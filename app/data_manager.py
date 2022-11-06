import requests
from config import SHEETY_PRICES_ENDPOINT

class DataManager:
    def __init__(self):
        self.destination_data = {}


    def get_sheety_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def post_sheety_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", 
                json=new_data
            )
        return response.status_code
