
import requests

# Dummy weather fetcher for a given ZIP code
def get_weather_forecast(zip_code: str):
    # Replace with real API key and request if integrating for production
    return {
        "zip": zip_code,
        "condition": "Cold and windy",
        "temperature": 42,
        "forecast_time": "2025-05-15T07:00:00Z"
    }
