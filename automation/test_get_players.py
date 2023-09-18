import requests
import pytest
import json

def test_read_player(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    response = requests.get(url)
    assert response.ok
    if response.ok:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print("response status code:", response.status_code)


