# Weather App

## Overview
This is a simple weather application built using Python's Tkinter library for the graphical user interface (GUI) and the OpenWeather API for fetching weather data. The app allows users to enter a city name and get real-time weather details such as temperature, weather description, "feels like" temperature, and humidity.

## Features
- **City Search**: Input the city name to fetch current weather data.
![Screenshot 2025-01-07 004331](https://github.com/user-attachments/assets/0801337e-4396-4821-9df4-5a2a4fc1d806)

- **Weather Information**: Displays weather description, temperature, "feels like" temperature, and humidity.
![Screenshot 2025-01-07 004419](https://github.com/user-attachments/assets/d2e949bc-a55e-4235-a40e-1e3f37bd095c)

- **Error Handling**: Alerts the user if the city is not found or if there is an issue with the data retrieval.
![Screenshot 2025-01-07 004451](https://github.com/user-attachments/assets/72dc855b-fa33-4f26-838a-2fa31921acc6)

## Requirements
- Python 3.x
- Tkinter library (usually comes pre-installed with Python)
- `requests` library to make API calls.

### Installing dependencies:
To install the required libraries, use the following commands:
```bash
pip install requests
```

## Setup
1. Clone or download the repository to your local machine.
2. Make sure you have an internet connection to access the OpenWeather API.
3. Replace the `API_key` in the code with your own OpenWeather API key. You can get one by signing up on [OpenWeather](https://openweathermap.org/).

## How to Run
1. Run the script using Python:
    ```bash
    python weather_app.py
    ```
2. The Tkinter window will pop up, allowing you to enter a city name and retrieve weather information.

## Customization
- You can customize the window’s appearance by changing the background color, fonts, and the overall layout using Tkinter options.

## Troubleshooting
- **City Not Found**: Ensure that the city name is entered correctly, including spelling and formatting (e.g., no extra spaces).
- **API Errors**: Check your internet connection and ensure the OpenWeather API key is correct.

## License
This project is open-source and free to use.
