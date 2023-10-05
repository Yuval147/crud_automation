import requests

from automation.test_get_players import test_read_player


def test_create_player(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    data = {
        "player_name": "test",
        "team": "test",
        "num_player": 111,
        "goals": 111,
        "assist": 111,
        "transfer_market": 1111112
    }
    response = requests.post(url, json= data)
    assert response.ok
    if response.ok:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print("response status code:", response.status_code)


    print("\nTesting Read Player API...")
    test_read_player(base_url)




