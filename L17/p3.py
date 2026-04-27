import requests

try:
    city = input("Enter the city name: ")

    # Step 1: Get latitude & longitude
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_response = requests.get(geo_url, params={"name": city, "count": 1})
    geo_data = geo_response.json()

    if "results" not in geo_data:
        print("City not found")
        exit()

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Step 2: Get weather data
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
    )

    data = weather_response.json()
    temperature = data["current_weather"]["temperature"]

    print(f"Temperature in {city}: {temperature}°C")

except Exception as e:
    print("Error:", e)

