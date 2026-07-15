from langchain.tools import tool
from datetime import datetime
import memory
from weather_tool import get_weather
import random

tools = [
    get_weather,
    calculator,
    search,
    wikipedia,
    memory
]