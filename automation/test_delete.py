import requests


def test_delete_player(base_url:str,id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint
    response = requests.delete(url)
    if response.status_code == 200:
        response_json = response.json()
        print("API successful")
        print(response_json)
    else:
        print("API failed")
        print("response status code:", response.status_code)
        print(response.content)



