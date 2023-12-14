from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from flask import Flask, request, render_template
import requests


views = Blueprint('views',__name__)

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeather
OPENWEATHER_API_KEY = '1ad5794b93b39b005cf9d22225230024'

@views.route('/weather', methods=['GET', 'POST'])
#@login_required
def weather():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        return render_template('weather.html', weather_data=weather_data)
    return render_template('weather.html', weather_data=None)

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
