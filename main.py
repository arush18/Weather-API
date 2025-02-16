import requests
import datetime as dt

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = open('api_key.txt', 'r').read()
city = str(input("Enter a city: "))
url = base_url + "appid=" + api_key + "&q=" + city

def k2cf(k):
    c = k-273.15
    f = c*(9/5)+32
    return c, f

response = requests.get(url).json()

longitude = response['coord']['lon']
latitude = response['coord']['lat']
kelvin = response['main']['temp']
celsius, fahrenheit = k2cf(kelvin)
humidity = response['main']['humidity']
desc = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']

print(f'-------------- {city} --------------')
print(f'---------- {longitude}, {latitude} ----------')
print(f'Temperature: {celsius:.2f}°C / {fahrenheit:.2f}°F')
print(f'Humidity: {humidity}%')
print(f'Speed of Wind: {wind_speed}m/s')
print(f'Local Sunrise Time: {sunrise_time}')
print(f'Local Sunset Time: {sunset_time}')
print(f'Weather Condition: {desc}')