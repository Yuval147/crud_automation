import requests

####### details value valid ########
def test_update_player(base_url:str, id:str ,valid_player_data):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data =valid_player_data
    response = requests.put(url, json=data,)
    if response.status_code == 200:
        response_json = response.json()
        print("API successful")
        print(response_json['id'])
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)

####### details value invalid ########
def test_update_player_detailsnotvalid(base_url:str, id:str ,invalid_player_data):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data =invalid_player_data
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
def test_update_player_opposites(base_url:str, id:str , opposite_player_data):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data = opposite_player_data
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
def test_update_player_nulldetails(base_url:str, id:str , null_player_data):
    endpoint = f"/{id}"
    url = base_url + endpoint
    data =null_player_data
    response = requests.put(url, json=data,)
    if response.status_code == 422:
        response_json = response.json()
        print("API successful")
        print(response_json['id'])
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)

