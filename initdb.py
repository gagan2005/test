#This file loads the csv and geojson into tables and runs some data initialization commands.
#Run this file only once
from sqlalchemy import create_engine
import urllib.request
from schemas import Places,createtables,boundaries
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
import json
meta=MetaData()
user="postgres"
password="abcd1234"
engine = create_engine("postgresql+psycopg2://"+user+":"+password+"@localhost/test")
conn=engine.connect()
# meta.create_all(engine)
createtables(engine)
Session = sessionmaker(bind = engine)
session = Session()

import csv

with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
data=data[1:]

table_entries=[]
for entry in data:
    table_entry=Places(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5])
    table_entries.append(table_entry)
session.add_all(table_entries)
session.commit()
query="create extension earthdistance cascade;"
try:
    conn.execute(query)   #Installs the earthdistance extension on postgres ,comment this if the extension is already installed
except:
    pass      
#Geojson part

with open('map.geojson') as f:
  data = json.load(f)
data=data['features']
for entry in data:
    b=boundaries(entry['properties']['name'],entry['properties']['type'],entry['properties']['parent'],entry['geometry']['coordinates'])
    session.add(b)
session.commit()
