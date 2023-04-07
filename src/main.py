import requests
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY')
url = "http://api.openweathermap.org/data/2.5/weather?"


#_______________________________________________// Créer une liste des villes de la France et appeler l'API \\___________________________________________
 
pays = ['Reims','Paris', 'Marseille', 'Lille', 'Rennes','Le Havre', 'Saint-Étienne', 'Toulon', 'Grenoble', 'Dijon', 'Angers', 'Nîmes', 'Villeurbanne','Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux']
weather_data = pd.DataFrame(columns=["City", "Temperature", "Feels Like", "Min Temp", "Max Temp", "Pressure", "Humidity", "Wind Speed", "Wind Direction", "Sunrise", "Sunset"])



for city in pays:
    api_url = url + "appid=" + API_KEY + "&q=" + city + "&units=metric" #API CALL 
    response = requests.get(api_url)   #Get method
    data = response.json()
    print(data)
    lon = data["coord"]["lon"]
    lat = data["coord"]["lat"]
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
    weather_data = weather_data.append({"City": city,"lon": lon, "lat" : lat, "Temperature": temperature, "Feels Like": feels_like, "Min Temp": min_temp, "Max Temp": max_temp, "Pressure": pressure, "Humidity": humidity, "Wind Speed": wind_speed, "Wind Direction": wind_direction, "Sunrise": sunrise, "Sunset": sunset}, ignore_index=True)


print(weather_data)


#________________________________________________// Créer un fishier CSV \\__________________________________________________________

weather_data.to_csv("weather_data.csv", index=False)  #EXport data as form CSV



#_______________________________________________// Créer une application sous Streamlit \\___________________________________________

#icone de la page web
st.set_page_config(page_title="Weather App", page_icon=":sunny:")
# ajouter un titre pour votre application
st.title("Current & Forecast weather data collection")
# Créer une carte folium centrée sur la France
m = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Ajouter un marqueur pour chaque ville
for index, row in weather_data.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['City']).add_to(m)

# Afficher la carte folium dans Streamlit
st_folium(m)

# Ajouter une liste déroulante pour sélectionner une ville
city = st.selectbox('Sélectionnez une ville', weather_data['City'])

# Récupérer les données météorologiques pour la ville sélectionnée
weather_data = weather_data[weather_data['City'] == city]

# Afficher les données météorologiques pour la ville sélectionnée
st.write('Température actuelle:', weather_data['Temperature'])
st.write('Température ressentie:', weather_data['Feels Like'])
st.write('Température minimale:', weather_data['Min Temp'])
st.write('Température maximale:', weather_data['Max Temp'])
st.write('Pression atmosphérique:', weather_data['Pressure'])
st.write('Humidité:', weather_data['Humidity'])
st.write('Vitesse du vent:', weather_data['Wind Speed'])
st.write('Direction du vent:', weather_data['Wind Direction'])
st.write('Sunrise:', weather_data['Sunrise'])
st.write('Sunset:', weather_data['Sunset'])

