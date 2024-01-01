import requests

####### details value valid ########
def test_create_player(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    data = {
        "player_name": "zlatan",
        "team": "milan",
        "num_player": 11,
        "goals": 11,
        "assist": 11,
        "transfer_market": 77777777,
        "country": "spain"
    }
    response = requests.post(url, json= data)
    if response.status_code == 200:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.text)
        print("response status code:", response.status_code)


####### details value not valid ########
def test_crate_player_detailsnotvalid(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    data = {
        "player_name": "zlatan",
        "team": "milan",
        "num_player": 111,
        "goals": 111,
        "assist": 111,
        "transfer_market": 1111112,
        "country": "spain"

    }
    response = requests.post(url, json= data)
    if response.status_code == 422:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.text)
        print("response status code:", response.status_code)



####### details value in the int put string ########
def test_crate_player_opposites(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    data = {
        "player_name": 12,
        "team": 12,
        "num_player": "111",
        "goals": "111",
        "assist": "111",
        "transfer_market": "1111112",
        "country": "spain"
    }
    response = requests.post(url, json= data)
    if response.status_code == 422:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.text)
        print("response status code:", response.status_code)

####### details value is null ########
def test_crate_player_nulldetails(base_url:str):
    endpoint = "/"
    url = base_url + endpoint
    data = {
        "player_name": None,
        "team": None,
        "num_player": 11,
        "goals": 11,
        "assist": 11,
        "transfer_market": 11,
        "country": "spain"
    }
    response = requests.post(url, json= data)
    if response.status_code == 422:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.text)
        print("response status code:", response.status_code)