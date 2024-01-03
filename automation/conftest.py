import pytest
import requests

@pytest.fixture(scope='session')
def base_url() -> str:
    return 'http://localhost:8600'

@pytest.fixture(scope='session')
def id(base_url:str) -> str:
    endpoint = "/"
    url = base_url + endpoint
    response = requests.get(url)
    assert response.ok
    if response.ok:
        response_json = response.json()
        player_id = response_json[0]['id']
        print(response_json)
        return player_id
    else:
        print("API failed")
        print("response status code:", response.status_code)

@pytest.fixture
def valid_player_data():
    return {
        "player_name": "zlatan",
        "team": "milan",
        "num_player": 11,
        "goals": 11,
        "assist": 11,
        "transfer_market": 77777777,
        "country": "spain"
    }

@pytest.fixture
def invalid_player_data():
    return {
        "player_name": "zlatan",
        "team": "milan",
        "num_player": 111,
        "goals": 111,
        "assist": 111,
        "transfer_market": 1111112,
        "country": "spain"
    }

@pytest.fixture
def opposite_player_data():
    return {
        "player_name": 12,
        "team": 12,
        "num_player": "111",
        "goals": "111",
        "assist": "111",
        "transfer_market": "1111112",
        "country": "spain"
    }

@pytest.fixture
def null_player_data():
    return {
        "player_name": None,
        "team": None,
        "num_player": 11,
        "goals": 11,
        "assist": 11,
        "transfer_market": 11,
        "country": "spain"
    }





