import requests


def test_update_player(base_url:str,id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data ={
    "player_name": "dolev",
    "team": "macabi",
    "id": 1,
    "assist": 2,
    "num_player": 8,
    "goals": 12,
    "transfer_market": 400000
  }
    response = requests.put(url, json=data,)
    assert response.ok
    if response.ok:
        response_json = response.json()
        print("API successful")
        print(response_json)
    else:
        print("API failed")
        print("response status code:", response.status_code)






