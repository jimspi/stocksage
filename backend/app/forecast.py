
from datetime import datetime, timedelta
import random

# Dummy model for demand prediction based on weather and trend signals
def predict_demand(item_id: str, historical_sales: list, weather_forecast: dict, tiktok_trend_score: float):
    base = sum(historical_sales[-7:]) / 7  # Average of last 7 days

    # Adjust for weather
    weather_multiplier = 1.1 if "cold" in weather_forecast.get("condition", "").lower() else 0.95

    # Adjust for trend
    trend_multiplier = 1 + min(tiktok_trend_score / 10, 0.25)  # cap trend boost at +25%

    # Add small random noise for demo purposes
    noise = random.uniform(-0.1, 0.1)

    forecast = base * weather_multiplier * trend_multiplier * (1 + noise)
    return round(forecast, 2)
