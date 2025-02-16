# Weather Report using OpenWeatherMap API

This is a simple Python script that fetches and displays the weather report for a given city using the OpenWeatherMap API.

## Features
- Fetches real-time weather data for any city.
- Displays temperature in Celsius and Fahrenheit.
- Shows humidity, wind speed, and weather conditions.
- Provides sunrise and sunset times adjusted to the local timezone.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- `requests` module (install using `pip install requests`)

## Setup
1. **Get OpenWeatherMap API Key**  
   - Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
   - Generate an API key from the API section.

2. **Save the API Key**  
   - Create a file named `api_key.txt` in the project directory.
   - Paste your API key into `api_key.txt` (without quotes or extra spaces).

## Usage
Run the script by executing the following command:

```sh
python weather_report.py
```

Then, enter the city name when prompted.

## Example Output
```
Enter a city: New York
-------------- New York --------------
---------- -74.01, 40.71 ----------
Temperature: 15.32°C / 59.58°F
Humidity: 78%
Speed of Wind: 3.5m/s
Local Sunrise Time: 2025-02-16 06:45:30
Local Sunset Time: 2025-02-16 17:30:15
Weather Condition: clear sky
```

## Notes
- Ensure that `api_key.txt` is in the same directory as the script.
- The script converts temperature from Kelvin to Celsius and Fahrenheit.
- The sunrise and sunset times are adjusted based on the city's timezone.

## License
This project is open-source and free to use under the MIT License.

## Author
Developed by **Arush**