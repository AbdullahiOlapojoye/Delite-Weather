from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '14fcace15cc3f4d7e4fbc5fc709779fa'

def get_weather(city=None, lat=None, lon=None):
    if city:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    elif lat and lon:
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    else:
        return None, "Error: No location provided"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), None
    else:
        return None, f"Error: {response.json().get('message', 'Unable to fetch data')}"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        lat = request.form.get('lat')
        lon = request.form.get('lon')
        
        if city:
            weather_data, error_message = get_weather(city=city)
        elif lat and lon:
            weather_data, error_message = get_weather(lat=lat, lon=lon)
        else:
            error_message = "Please provide a city name or allow location access."

    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)