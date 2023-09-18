import requests


def test_delete_player(base_url:str,id:str):
    endpoint = f"/{id}"
    url = base_url + endpoint

    response = requests.put(url,)
    assert response.ok
    if response.ok:
        response_json = response.json()
        print("API successful")
        print(response_json)
    else:
        print("API failed")
        print("response status code:", response.status_code)



