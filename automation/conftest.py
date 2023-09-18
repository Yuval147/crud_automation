import pytest
import requests
import json

@pytest.fixture(scope='session')
def base_url() -> str:
    return 'http://localhost:9000'

@pytest.fixture(scope='session')
def id(base_url:str) -> str:
    endpoint = "/"
    url = base_url + endpoint
    response = requests.get(url)
    assert response.ok
    if response.ok:
        response_json = response.json()
        print(response_json)
        player_id = response_json[0]['id']
        return player_id
    else:
        print("API failed")
        print("response status code:", response.status_code)




