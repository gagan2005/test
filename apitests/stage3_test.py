import requests
import pytest
apiurl = "http://127.0.0.1:8000/"


def test_detect_1():
     lat=28.6137
     lng=77.23
     response=requests.get(apiurl+"detect?lat="+str(lat)+"&lng="+str(lng))
     # print(response)
     assert response.status_code == 200
     response=response.json()
     # print(response)
     assert response['place'] == 'Central Delhi'

# test_detect_1()