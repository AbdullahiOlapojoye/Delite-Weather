# Delite-Weather
This is a web-based weather application built using Flask, Python, and the OpenWeatherMap API. The app allows users to get real-time weather information and a 5-day forecast for any city they enter, or based on their current location.

## Features

- **City-Based Search:** Enter any city to fetch the current weather and a 5-day forecast.
- **Location-Based Search:** Use your current geographic location to get weather updates instantly.
- **Responsive Design:** Optimized for all devices, ensuring a seamless experience on mobile, tablet, and desktop.
- **Error Handling:** Displays user-friendly error messages for invalid city names or when location data cannot be retrieved.
- **Dynamic Weather Icons:** Visually appealing weather icons represent different weather conditions.

## Technologies Used

- **Python & Flask:** For the backend logic and API integration.
- **HTML/CSS/JavaScript:** For the frontend and responsive design.
- **OpenWeatherMap API:** To fetch real-time weather data and forecasts.
  
## Setup Instructions

### 1. Clone the Repository to your local machine
### 2. Create and Configure the .env File and fill with: OPENWEATHER_API_KEY= 'put_your_open_weather_api_key_here' (Get api key from https://openweathermap.org/)
### 3. Install dependencies 
- create a virtual environment: python -m venv venv
- Activate the virtual environment: venv\Scripts\activate (Windows) or source venv/bin/activate (MacOS)
- Install the requirements: pip install -r requirements.txt
### 4. Run application
