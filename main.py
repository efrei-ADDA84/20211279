from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")


@app.route("/")
def get_current_weather():
    lat = request.args.get("lat", default=None, type=float)
    lon = request.args.get("lon", default=None, type=float)

    if lat is None or lon is None:
        return "Error: missing 'lat' or 'lon' parameter"

    weather_data = get_weather(API_KEY, lat, lon)

    if "error" in weather_data:
        return weather_data, 500
    else:
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
            "error": f"Error retrieving weather data , {response.status_code} - {response.reason}"
        }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
