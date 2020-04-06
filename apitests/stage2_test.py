import requests
# import pytest
import random
apiurl="http://127.0.0.1:8000/"
def test_usingself():
    lat=23.22
    lng=77.6
    radius=16
    url="{0}?lat={1}&lng={2}&radius={3}".format("get_using_self",lat,lng,radius)
    response=requests.get(apiurl+url)
    assert response.status_code == 200
    response=response.json()
    assert len(response) == 2

def test_usingpostgres():
    lat=23.22
    lng=77.6
    radius=16
    url="{0}?lat={1}&lng={2}&radius={3}".format("get_using_postgres",lat,lng,radius)
    print(url)
    response=requests.get(apiurl+url)
    assert response.status_code == 200
    response=response.json()
    assert len(response) == 2

def test_comapre_both():
    for _ in range(100):
        lng=77+random.random()
        lat=23+random.random()*2
        radius=10
        url="{0}?lat={1}&lng={2}&radius={3}".format("get_using_self",lat,lng,radius)
        response=requests.get(apiurl+url)
        assert response.status_code == 200
        response=response.json()
        url="{0}?lat={1}&lng={2}&radius={3}".format("get_using_self",lat,lng,radius)
        response2=requests.get(apiurl+url).json()
        assert response2 == response
