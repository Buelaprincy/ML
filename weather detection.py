import requests

# Enter your API key here
api_key = "3c674e8b5ddd80c417fe5298d3ac6a09"
Base_url = "https://api.openweathermap.org/data/2.5/weather"

# Enter city name
city = input("what city do you know the weather?")

# Construct final URL
url = f"{Base_url}appid={api_key}q={city}"

# Send GET request
response = requests.get(url)

# Parse JSON response
print(response.json())
if  response.status_code == 200:
    data = response.json()
    main = data['main']
    weather_desc = data['weather'][0]['description']
    temperature = main['temp']
    humidity = main['humidity']
    pressure = main['pressure']
    wind_speed = data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"pressure:{pressure}hPa")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {weather_desc.capitalize()}")
else:
    print("something went wrong. Please check the name.")