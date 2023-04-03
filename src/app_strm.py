# import folium
# import pandas as pd
# import requests
# import json
# import os
# from dotenv import load_dotenv
# load_dotenv()


# API_KEY = os.getenv('API_KEY')
# url = "http://api.openweathermap.org/data/2.5/weather?"



# # Créer une carte centrée sur la France
# m = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# # Charger les données des villes
# df = pd.read_csv("weather_data.csv")

# # Ajouter un marker pour chaque ville
# for index, row in df.iterrows():
#     ville = row["ville"]
#     lat = row["latitude"]
#     lon = row["longitude"]
#     marker = folium.Marker(location=[lat, lon], popup=ville)
#     marker.add_to(m)

# # Afficher la carte
# m

# # Récupérez les coordonnées de la ville sélectionnée à partir de votre DataFrame
# lat = df.loc[df['ville'] == selected_city, 'latitude'].iloc[0]
# lon = df.loc[df['ville'] == selected_city, 'longitude'].iloc[0]

# # Construisez l'URL de l'API OpenWeatherMap en utilisant les coordonnées de la ville et votre clé API
# api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

# # Effectuez une requête à l'API OpenWeatherMap
# response = requests.get(api_url)

# # Analysez la réponse JSON de l'API OpenWeatherMap
# data = json.loads(response.text)

# # Extrayez les informations météorologiques pertinentes de la réponse JSON
# temperature = data['main']['temp']
# humidity = data['main']['humidity']
# pressure = data['main']['pressure']
# weather_description = data['weather'][0]['description']

# # Stockez les informations météorologiques dans un DataFrame de pandas, selon vos besoins
# weather_data = pd.DataFrame({
#     'ville': [selected_city],
#     'temperature': [temperature],
#     'humidity': [humidity],
#     'pressure': [pressure],
#     'weather_description': [weather_description]
# })

