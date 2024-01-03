import requests

####### details value valid ########
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

####### details value not valid ########
def test_update_player_detailsnotvalid(base_url:str, id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data ={
    "player_name": "dolev haziza",
    "team": "macabi",
    "id": 5,
    "assist": 2222,
    "num_player": 8222,
    "goals": 1222,
    "transfer_market": 400000,
    "country": "spain"
    }
    response = requests.put(url, json=data,)
    if response.status_code == 422:
        response_json = response.json()
        print("API successful")
        print(response_json['id'])
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)

####### details value in the int put string ########
def test_update_player_opposites(base_url:str, id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data ={
    "player_name": 12,
    "team": 12,
    "id": 5,
    "num_player": "111",
    "goals": "111",
    "assist": "111",
    "transfer_market": "1111112",
    "country": "spain"
    }
    response = requests.put(url, json=data,)
    if response.status_code == 422:
        response_json = response.json()
        print("API successful")
        print(response_json['id'])
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)


####### details value is null ########
def test_update_player_nulldetails(base_url:str, id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data ={
    "player_name": None,
    "team": None,
    "num_player": 11,
    "goals": 11,
    "assist": 11,
    "transfer_market": 11,
    "country": "spain"
    }
    response = requests.put(url, json=data,)
    if response.status_code == 422:
        response_json = response.json()
        print("API successful")
        print(response_json['id'])
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)

