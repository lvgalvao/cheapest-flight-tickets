from data_manager import DataManager
from flight_search import FlightSearch

import pprint

dataManager = DataManager()
flightSearch = FlightSearch()
# sheet_data = dataManager.get_sheety_data()
sheet_data = [
    {"city": "Paris", "iataCode": "CDG", "lowestPrice": 54, "id": 2},
    {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
    {"city": "Tokyo", "iataCode": "NRT", "lowestPrice": 485, "id": 4},
    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
    {"city": "Istanbul", "iataCode": "SAW", "lowestPrice": 95, "id": 6},
    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
    {"city": "New York", "iataCode": "JFK", "lowestPrice": 240, "id": 8},
    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
]

pp = pprint.PrettyPrinter(indent=4)

if sheet_data[0]["iataCode"] == "":
    cities = []
    for rows in range(len(sheet_data)):
        cities.append(sheet_data[rows]["city"])
        # print(cities)
    iata_code = flightSearch.get_iata_code(cities)
    for rows in range(len(sheet_data)):
        sheet_data[rows]["iataCode"] = iata_code[rows]
    new_sheet_data = dataManager.post_sheety_data(datasheet=sheet_data)
    # pp.pprint(new_sheet_data)

fs = FlightSearch()
fs.get_cheap_flights(sheet_data)