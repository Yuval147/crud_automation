import requests

def test_create_player(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    data = {
        "player_name": "yuval yanous",
        "team": "maccabi",
        "num_player": 7,
        "goals": 50,
        "assist": 20,
        "transfer_market": 777777
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

