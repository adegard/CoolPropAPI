from flask import Flask, request, jsonify
import CoolProp.CoolProp as CP

app = Flask(__name__)

@app.route('/get-property', methods=['GET'])
def get_property():
    fluid = request.args.get('fluid')
    prop = request.args.get('prop')
    temp = float(request.args.get('temp'))
    pressure = float(request.args.get('pressure', 101325))

    print(f"Requesting: PropsSI({prop}, 'T', {temp}, 'P', {pressure}, {fluid})")  # Debugging output

    try:
        value = CP.PropsSI("Cpmass", "T", 300, "P", 101325, "Water")
        return jsonify({'fluid': fluid, 'property': prop, 'value': value})
    except Exception as e:
        return jsonify({'error': str(e)})

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
