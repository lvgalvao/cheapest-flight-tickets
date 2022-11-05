import requests

import sys
sys.path.append("./app")

from app.config import SHEETY_PRICES_ENDPOINT
from app.data_manager import DataManager

sheet_data_test = [
    {"city": "Paris", "iataCode": "CDG", "lowestPrice": 54, "id": 2},
    {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
    {"city": "Tokyo", "iataCode": "NRT", "lowestPrice": 485, "id": 4},
    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
    {"city": "Istanbul", "iataCode": "SAW", "lowestPrice": 95, "id": 6},
    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
    {"city": "New York", "iataCode": "JFK", "lowestPrice": 240, "id": 8},
    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
    {'city': 'São Paulo', 'iataCode': '', 'id': 11, 'lowestPrice': 100}
]

def test_get_sheet_data_api_get_works():
    response = requests.get(url=SHEETY_PRICES_ENDPOINT)
    # data = response.json()["prices"]
    assert response.status_code == 200
    # assert data == sheet_data_test


def test_get_sheet_data_type_is_list():
    DM = DataManager()
    sheet_data = DM.get_sheety_data()
    assert type(sheet_data) == list


def test_get_sheet_data_content_has_city_iataCode_id_lowestPrice_columns():
    DM = DataManager()
    sheet_data = DM.get_sheety_data()
    assert ("city" in sheet_data[0]) == True
    assert ("iataCode" in sheet_data[0]) == True
    assert ("id" in sheet_data[0]) == True
    assert ("lowestPrice" in sheet_data[0]) == True
