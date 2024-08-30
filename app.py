from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '14fcace15cc3f4d7e4fbc5fc709779fa' 

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def get_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = get_weather(city)
        forecast_data = get_forecast(city)
    return render_template('index.html', weather=weather_data, forecast=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)