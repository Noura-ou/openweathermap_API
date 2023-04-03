import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY')
url = "http://api.openweathermap.org/data/2.5/weather?"


pays = ['Reims','Paris', 'Marseille', 'Lille', 'Rennes','Le Havre', 'Saint-Étienne', 'Toulon', 'Grenoble', 'Dijon', 'Angers', 'Nîmes', 'Villeurbanne','Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux']
weather_data = pd.DataFrame(columns=["City", "Temperature", "Feels Like", "Min Temp", "Max Temp", "Pressure", "Humidity", "Wind Speed", "Wind Direction", "Sunrise", "Sunset"])


for city in pays:
    api_url = url + "appid=" + API_KEY + "&q=" + city + "&units=metric" #API CALL 
    response = requests.get(api_url)   #Get method
    data = response.json()
    # print(data)
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    min_temp = data["main"]["temp_min"]
    max_temp = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_direction = data["wind"]["deg"]
    sunrise = pd.to_datetime(data["sys"]["sunrise"], unit='s')
    sunset = pd.to_datetime(data["sys"]["sunset"], unit='s')
    weather_data = weather_data.append({"City": city, "Temperature": temperature, "Feels Like": feels_like, "Min Temp": min_temp, "Max Temp": max_temp, "Pressure": pressure, "Humidity": humidity, "Wind Speed": wind_speed, "Wind Direction": wind_direction, "Sunrise": sunrise, "Sunset": sunset}, ignore_index=True)


print(weather_data)

weather_data.to_csv("weather_data.csv", index=False)  #EXport data as form CSV

