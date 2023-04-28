from flask import Flask, jsonify
import config
import requests

app = Flask(__name__)


@app.route("/weather")
def get_current_weather():
    lat = config.LAT
    lon = config.LONG
    api_key = config.API_KEY
    weather_data = get_weather(api_key, lat, lon)

    return jsonify(weather_data)


def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_data = {
            "description": description,
            "temp": temp,
            "feels_like": feels_like,
            "humidity": humidity,
        }
        return weather_data
    else:
        return {
            "error": f"Error retrieving weather data , {response.status_code}-{response.reason}"
        }


if __name__ == "__main__":
    app.run(debug=True)
