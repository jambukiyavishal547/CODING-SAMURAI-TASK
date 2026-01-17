import requests

API_KEY = "e5d06644ac711e4977785013774e9f42"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("\nEnter city name (or 'exit'): ").strip()

    if city.lower() == "exit":
        break

    params = {
        "q": f"{city},IN",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\n📍 City: {data['name']}")
            print(f"🌡 Temp: {data['main']['temp']}°C")
            print(f"💧 Humidity: {data['main']['humidity']}%")
            print(f"☁ Weather: {data['weather'][0]['description']}")
        else:
            print("❌ API Error:", data.get("message"))

    except requests.exceptions.RequestException:
        print("❌ Network error")
