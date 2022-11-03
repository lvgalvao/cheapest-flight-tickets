import requests

from config import SHEETY_PRICES_ENDPOINT


class DataManager:
    def __init__(self):
        pass

    def get_sheety_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()["prices"]
        return data

    def post_sheety_data(self, datasheet: list):
        for n in range(len(datasheet)):
            new_data = {"price": datasheet[n]}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{datasheet[n]['id']}", json=new_data
            )
        return response.status_code
