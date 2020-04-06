from math import radians,acos,sin,cos
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
import json
def dist(lat1,lng1,lat2,lng2):
    lat1=radians(lat1)
    lng1=radians(lng1)
    lat2=radians(lat2)
    lng2=radians(lng2)
    d = 3963.0 * acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(lng2-lng1))
    return d

def findplace(res,lat,lng):
    for entry in res:
        x=entry.geometry.replace('{','[').replace('}',']')
        x=json.loads(x)
        x=x[0]
        point=Point(lat,lng)
        # print(point)
        points=[]
        # print("Entry name"+entry.name)
        for y in x:
            p=Point(y[1],y[0])
            points.append(p)
            print(p)
            # print("\t"+str(p))
        polygon=Polygon(points)
        # print(polygon.distance(point))
        # print(polygon.contains(point))
        if(polygon.contains(point)):
            return entry
    return None
