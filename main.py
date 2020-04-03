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
d=0.005
class Pla(BaseModel):
    lat:float
    lng:float
    pin:str
    address:str
    city:str


@app.post('/post_location')
async def create_place(place : Pla):
   
    res=session.query(schemas.Places).\
        filter(schemas.Places.key==place.pin)
    res2=session.query(schemas.Places).\
        filter(\
        schemas.Places.latitude>place.lat-d,\
        schemas.Places.latitude<place.lat+d,\
        schemas.Places.longitude>place.lng-d,\
        schemas.Places.longitude<place.lng+d )
    if(res.count()!=0):
        return "Pin already exists"
    if(res2.count()!=0):
        return "Location already exists"
    p=schemas.Places(key=place.pin,admin_name1=place.city,latitude=place.lat,longitude=place.lng,place_name=place.address)
    session.add(p)
    try:
        session.commit()
    except:
        return "Some Error Occured"
    return "Added Succesfully"

@app.get('/get_location')
async def getrow(lat:float,lng:float):
    res=session.query(schemas.Places).\
        filter(schemas.Places.latitude.in_([lat-d,lat+d])\
            ,schemas.Places.longitude.in_([lng-d,lng+d]))
    if(res.count()==0):
        return "not found"
    else:
        ans={}
        l=res.all()[0]
        ans['pin_code']=l.key
        ans['city']=l.admin_name1
        ans['address']=l.place_name
        return ans

