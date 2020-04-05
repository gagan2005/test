from sqlalchemy import Column, Integer, String,Float,Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Places(Base):
    __tablename__="places"
    def __init__(self,key,place_name,admin_name1,latitude,longitude,accuracy=-1):
        if(accuracy==""):
            accuracy=-1
        if(latitude==""):
            latitude=-1
        if(longitude==""):
            longitude=-1
        self.key=key
        self.place_name=place_name
        self.admin_name1=admin_name1
        self.latitude=latitude
        self.longitude=longitude
        self.accuracy=accuracy
    key=Column(String,primary_key=True)
    place_name=Column(String)
    admin_name1=Column(String)
    latitude=Column(Float)
    longitude=Column(Float)
    accuracy=Column(Float)

class boundaries(Base):
    __tablename__="boundaries"
    name=Column(String,primary_key=True)
    Type=Column(String)
    parent=Column(String)
    geometry=Column(Text)
    def __init__(self,name,Type,parent,geometry):
        self.name=name
        self.Type=Type
        self.parent=parent
        self.geometry=geometry


def createtables(engine):
    Base.metadata.create_all(engine)