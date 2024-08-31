import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv  # Import the load_dotenv function

# Load the .env file
load_dotenv()

app = Flask(__name__)

# Fetch API Key from environment variable
API_KEY = os.getenv('OPENWEATHER_API_KEY')

if not API_KEY:
    raise ValueError("No API key found. Set the OPENWEATHER_API_KEY environment variable.")

def get_weather_and_forecast(city=None, lat=None, lon=None):
    if city:
        location_query = f'q={city}'
    elif lat and lon:
        location_query = f'lat={lat}&lon={lon}'
    else:
        return None, "Invalid location data"

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?{location_query}&appid={API_KEY}&units=metric'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?{location_query}&appid={API_KEY}&units=metric'
    
    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code == 200 and forecast_response.status_code == 200:
        return {
            'weather': weather_response.json(),
            'forecast': forecast_response.json()
        }, None
    elif weather_response.status_code == 404:
        return None, "City not found. Please check the name and try again."
    elif weather_response.status_code == 429:
        return None, "API rate limit exceeded. Please try again later."
    else:
        return None, f"Error: {weather_response.status_code} - {weather_response.json().get('message', 'Unable to fetch data')}"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            result, error_message = get_weather_and_forecast(city=city)
            if result:
                weather_data = result['weather']
                forecast_data = result['forecast']
        else:
            error_message = "Please enter a city name."

    return render_template('index.html', weather=weather_data, forecast=forecast_data, error=error_message)

@app.route('/location', methods=['POST'])
def location_weather():
    lat = request.json.get('lat')
    lon = request.json.get('lon')

    if not lat or not lon:
        return jsonify({'error': "Invalid location data"}), 400

    result, error_message = get_weather_and_forecast(lat=lat, lon=lon)

    if error_message:
        return jsonify({'error': error_message}), 400
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)