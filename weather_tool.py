import os
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    Get the current weather of a city.
    """
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY").strip()


@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    Use this whenever the user asks about weather or provides only a city name.
    """

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return f"Couldn't find weather for '{city}'."

    data = response.json()

    return (
        f"Weather in {city}\n"
        f"Temperature: {data['main']['temp']}°C\n"
        f"Condition: {data['weather'][0]['description']}\n"
        f"Humidity: {data['main']['humidity']}%"
    )