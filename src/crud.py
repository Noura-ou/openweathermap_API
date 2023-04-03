from sqlalchemy import create_engine
import sqlite3
import pandas as pd

#______________________________________// Créer une base de données SQL \\___________________________________________

# Créer une connexion à la base de données
connection = sqlite3.connect("weather_base.db")

# Nom de la table dans la base de données
sql_table = 'weather_data_SQL'

# Charger les données dans un DataFrame
df = pd.read_csv("weather_data.csv")

# Écrire le DataFrame dans la table SQL
df.to_sql(sql_table, connection, if_exists='replace')

# Fermer la connexion à la base de données
connection.close()

