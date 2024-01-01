import requests


def test_update_player(base_url:str, id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data ={
    "player_name": "dolev haziza",
    "team": "macabi",
    "id": 5,
    "assist": 2,
    "num_player": 8,
    "goals": 12,
    "transfer_market": 400000,
    "country": "spain"
    }
    response = requests.put(url, json=data,)
    if response.status_code == 200:
        response_json = response.json()
        print("API successful")
        print(response_json['id'])
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)






