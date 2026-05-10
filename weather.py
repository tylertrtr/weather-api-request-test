import requests

coords = {"latitude": 34.0203686, "longitude": -118.5768803}

url = f"https://api.open-meteo.com/v1/forecast?latitude={coords["latitude"]}&longitude={coords["longitude"]}&daily=temperature_2m_min,temperature_2m_max&current=temperature_2m&timezone=auto&temperature_unit=fahrenheit"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Coordinates: {data["latitude"]}°N {data["longitude"]}°E")
    print(f"Timezone: {data["timezone"]} ({data["timezone_abbreviation"]})")
    print("----")
    print(f"Current time: {data["current"]["time"][-5:]}")
    print(f"Current temperature: {data["current"]["temperature_2m"]}°F")
    print("----")
    print("7-day forecast:")
    for i, day in enumerate(data["daily"]["time"]):
        print(f" {day}: {data["daily"]["temperature_2m_min"][i]}°F - {data["daily"]["temperature_2m_max"][i]}°F")
else:
    print(f"Failed to retrieve data {response.status_code}")