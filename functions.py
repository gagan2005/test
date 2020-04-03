from math import radians,acos,sin,cos
def dist(lat1,lng1,lat2,lng2):
    lat1=radians(lat1)
    lng1=radians(lng1)
    lat2=radians(lat2)
    lng2=radians(lng2)
    d = 3963.0 * acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(lng2-lng1))
    return d

print(dist(1,2,2,1))