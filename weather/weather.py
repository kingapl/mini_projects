import requests

city = input("Weather for the city: ")

city_url = f"https://www.metaweather.com/api/location/search/?query={city}"

city_response = requests.get(city_url)
city_response_dict = city_response.json()
city_info = city_response_dict[0]
city_id = city_info['woeid']

weather_url = f"https://www.metaweather.com/api/location/{city_id}/"
response = requests.get(weather_url)

response_dict = response.json()
weather_info = response_dict['consolidated_weather']
today = weather_info[0]

date = today['applicable_date']
the_temp = today['the_temp']
wind_speed = today['wind_speed']
air_pressure = today['air_pressure']

print(f"\nToday: {date}")
print(f"Temperature: {the_temp} C")
print(f"Wind speed: {int(wind_speed)} mph")
print(f"Air pressure: {int(air_pressure)} mbar")