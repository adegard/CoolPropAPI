from flask import Flask, request, jsonify
import CoolProp.CoolProp as CP

app = Flask(__name__)

@app.route('/get-property', methods=['GET'])
def get_property():
    fluid = request.args.get('fluid')
    prop = request.args.get('prop')
    temp = float(request.args.get('temp'))  # Temperature in Kelvin
    pressure = float(request.args.get('pressure', 101325))  # Default pressure in Pascals
    pressure_out = float(request.args.get('pressure_out', 101325))  # Outlet pressure for isentropic calculation
    
    try:
        # If requesting Psat, use saturation property
        if prop.lower() == "psat":
            value = CP.PropsSI("P", "T", temp, "Q", 0, fluid)  # Saturation pressure at temp
        
        # If requesting His (isentropic enthalpy), calculate based on entropy conservation
        elif prop.lower() == "his":
            # Get entropy (S1) at initial pressure and enthalpy
            entropy = CP.PropsSI("S", "P", pressure, "H", CP.PropsSI("H", "T", temp, "P", pressure, fluid), fluid)
            
            # Get isentropic enthalpy at new pressure
            value = CP.PropsSI("H", "P", pressure_out, "S", entropy, fluid)

        else:
            # Default property retrieval
            value = CP.PropsSI(prop, 'T', temp, 'P', pressure, fluid)

        return jsonify({'fluid': fluid, 'property': prop, 'value': value})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
