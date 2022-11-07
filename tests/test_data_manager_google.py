from app.data_manager_google import DataManager

sheet_data_test = [
    {"city": "Paris", "iataCode": "CDG", "lowestPrice": '54', "id": '2'},
    {"city": "Berlin", "iataCode": "BER", "lowestPrice": '42', "id": '3'},
    {"city": "Tokyo", "iataCode": "NRT", "lowestPrice": '485', "id": '4'},
    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": '551', "id":'5'},
    {"city": "Istanbul", "iataCode": "SAW", "lowestPrice": '95', "id": '6'},
    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": '414', "id": '7'},
    {"city": "New York", "iataCode": "JFK", "lowestPrice": '240', "id": '8'},
    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": '260', "id": '9'},
    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": '378', "id": '10'}
]

def test_get_sheet_data_type_is_list():
    DM = DataManager()
    sheet_data = DM.get_sheety_data()
    assert sheet_data == sheet_data_test