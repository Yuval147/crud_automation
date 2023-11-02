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


def test_get_random(base_url:str):

    endpoint = "/"
    url = base_url + endpoint
    r = requests.get(url)
    data = json.loads(r.text)

    players_list = []

    for players in data:
        player_name = players ['player_name']

        player_item = {
            'player_name': player_name
        }
        players_list.append(player_item)


    print(players_list)




