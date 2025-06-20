## Setting up a CoolProp-based web API for Google Sheets ( CoolProp wrapper)

We'll create a Python Flask web service that runs CoolProp, then connect it to Google Apps Script so you can call fluid properties directly in Google Sheets.

# Step 1: Set Up Your Python Flask Server
Install Flask and CoolProp on your server and tranfer 

coolprop_api.py

requirement.txt file


# Step 2: Deploy the API
To make this accessible from Google Sheets, host the Flask server on a cloud provider like:

- Render (free deployment)

- Heroku (easy setup)

- Google Cloud (strong integration)

- AWS Lambda + API Gateway (serverless option)

Once deployed, the API will be available at:

https://your-server.com/get-property

# Step 3: Connect Google Apps Script to the API
Now, create a Google Apps Script function in Google Sheets to call the API:

 ```js
function getFluidProperty(fluid, prop, temp, pressure) {
  var url = "https://your-server.com/get-property?fluid=" + fluid + "&prop=" + prop + "&temp=" + temp + "&pressure=" + pressure;
  
  var response = UrlFetchApp.fetch(url);
  var data = JSON.parse(response.getContentText());
  
  if (data.error) {
    return "Error: " + data.error;
  } else {
    return data.value;  // Return the property value
  }
}
 ```
# How to Use It in Google Sheets
In any google sheet cell:


 ```=getFluidProperty("Water", "Cpmass", 300, 101325) ```

💡 This calls CoolProp remotely and retrieves specific heat (CP) of water at 300K and 1 atm.

http://www.coolprop.org/index.html
