import requests
import os

API_KEY = os.environ.get("API_KEY")
LAT = os.environ.get("LAT")
LONG = os.environ.get("LONG")


def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        return f"Current weather: {description}, temperature: {temp}, feels like: {feels_like}, humidity: {humidity}"
    else:
        return (
            f"Error retrieving weather data , {response.status_code}-{response.reason}"
        )


if __name__ == "__main__":
    print("your params are :", API_KEY, LAT, LONG)
    print(get_weather(API_KEY, LAT, LONG))
