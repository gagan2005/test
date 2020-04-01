from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import schemas
user="postgres"
password="abcd1234"
engine = create_engine("postgresql+psycopg2://"+user+":"+password+"@localhost/test",echo=True)
engine.connect()
Session = sessionmaker(bind = engine)
session = Session()
app = FastAPI()
class Pla(BaseModel):
    lat:float
    lon:float
    pin:str
    address:str
    city:str


@app.post('/post_location')
async def create_place(place : Pla):
    p=schemas.Places(key=place.pin,admin_name1=place.city,latitude=place.lat,longitude=place.lon,place_name=place.address)
    session.add(p)
    session.commit()
    return 1
