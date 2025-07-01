import requests

def get_weather(city):
    try:
        # Use wttr.in with JSON format (no API key needed)
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]

            print(f"\n🌤 Weather in {city.capitalize()}:\n")
            print(f"Temperature      : {current['temp_C']}°C")
            print(f"Feels Like       : {current['FeelsLikeC']}°C")
            print(f"Condition        : {current['weatherDesc'][0]['value']}")
            print(f"Humidity         : {current['humidity']}%")
            print(f"Wind             : {current['windspeedKmph']} km/h {current['winddir16Point']}")
            print(f"Cloud Cover      : {current['cloudcover']}%")
        else:
            print("Failed to retrieve weather data. Please check the city name.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("🌐 Simple Weather App (wttr.in)")
    city = input("Enter city name: ").strip()
    get_weather(city)
