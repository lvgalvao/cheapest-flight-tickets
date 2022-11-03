from app.data_manager import DataManager
from conf.config import SHEETY_PRICES_ENDPOINT
import requests


def test_get_sheet_data_api_get_works():
    response = requests.get(url=SHEETY_PRICES_ENDPOINT)
    assert response.status_code == 200


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
