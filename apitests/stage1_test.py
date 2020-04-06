import requests
import pytest
apiurl="http://127.0.0.1:8000/"
def test_getlocation_1():
    lat=23
    lng=73
    response=requests.get(apiurl+"get_location?lat="+str(lat)+"&lng="+str(lng))
    assert response.status_code == 200

def test_getlocation_2():       #Trying an already present location
    lat=28.8
    lng=77.15
    response=requests.get(apiurl+"get_location?lat="+str(lat)+"&lng="+str(lng))
    assert response.status_code == 200
    # print(response)
    response=response.json()
    # print(response)
    assert response['pin_code'] == "IN/110036"

def test_getlocation_3():       #Trying a location very close to already present location
    lat=28.799
    lng=77.148
    response=requests.get(apiurl+"get_location?lat="+str(lat)+"&lng="+str(lng))
    assert response.status_code == 200
    response=response.json()
    assert response['pin_code'] == "IN/110036"

def test_getlocation_4():       #Trying a location that is not present in the table
    lat=100
    lng=100
    response=requests.get(apiurl+"get_location?lat="+str(lat)+"&lng="+str(lng))
    assert response.status_code == 200
    assert response.text == '"not found"'
# test_getlocation_2()