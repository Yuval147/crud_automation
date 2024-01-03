import requests



####### details value valid ########
def test_create_player(base_url:str , valid_player_data):
    endpoint = "/"
    url = base_url + endpoint
    data = valid_player_data
    response = requests.post(url, json= data)
    if response.status_code == 200:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.content)
        print("response status code:", response.status_code)


####### details value invalid ########
def test_crate_player_detailsnotvalid(base_url:str , invalid_player_data):
    endpoint = "/"
    url = base_url + endpoint
    data = invalid_player_data
    response = requests.post(url, json= data)
    if response.status_code == 422:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.content)
        print("response status code:", response.status_code)



####### details value in the int put string ########
def test_crate_player_opposites(base_url:str ,opposite_player_data):
    endpoint = "/"
    url = base_url + endpoint
    data = opposite_player_data
    response = requests.post(url, json= data)
    if response.status_code == 422:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.content)
        print("response status code:", response.status_code)

####### details value is null ########
def test_crate_player_nulldetails(base_url:str , null_player_data):
    endpoint = "/"
    url = base_url + endpoint
    data = null_player_data
    response = requests.post(url, json= data)
    if response.status_code == 422:
        json_response = response.json()
        print("API successful")
        print(json_response)
    else:
        print("API failed")
        print(response.content)
        print("response status code:", response.status_code)