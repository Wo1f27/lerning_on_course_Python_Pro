import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_TOKEN')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city):
    try:
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        response.raise_for_status()
        data = response.json()

        weather_info = {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        return weather_info
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных для города {city}: {e}")
        return None
