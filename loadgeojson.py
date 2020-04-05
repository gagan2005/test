
import json
from sqlalchemy import create_engine
import urllib.request
from schemas import boundaries,createtables
from sqlalchemy.orm import sessionmaker
# meta=Metaentry()
user="postgres"
password="abcd1234"
engine = create_engine("postgresql+psycopg2://"+user+":"+password+"@localhost/test")
engine.connect()
# meta.create_all(engine)
createtables(engine)
Session = sessionmaker(bind = engine)
session = Session()


with open('map.geojson') as f:
  data = json.load(f)
data=data['features']
for entry in data:
    # entry=entry['properties']
    # print((entry['geometry']['coordinates']))
    # break
    b=boundaries(entry['properties']['name'],entry['properties']['type'],entry['properties']['parent'],entry['geometry']['coordinates'])
    session.add(b)
session.commit()

