from sqlalchemy import create_engine
import urllib.request
from schemas import Places,createtables
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
meta=MetaData()
user="postgres"
password="abcd1234"
engine = create_engine("postgresql+psycopg2://"+user+":"+password+"@localhost/test")
engine.connect()
# meta.create_all(engine)
createtables(engine)
Session = sessionmaker(bind = engine)
session = Session()

# url="http://raw.githubusercontent.com//sanand0/pincode/blob/master/data/IN.csv"
# wget.download(url,"./")
# urllib.request.urlretrieve(url, '/')
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

