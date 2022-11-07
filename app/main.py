import datetime
import pprint

# from data_manager import DataManager
from flight_search import FlightSearch
from data_manager_google import DataManager


dataManager = DataManager()
flightSearch = FlightSearch()
sheet_data = dataManager.get_sheety_data()
# # sheet_data = [
#     {"city": "Paris", "iataCode": "CDG", "lowestPrice": 54, "id": 2},
#     {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
#     {"city": "Tokyo", "iataCode": "NRT", "lowestPrice": 485, "id": 4},
#     {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
#     {"city": "Istanbul", "iataCode": "SAW", "lowestPrice": 95, "id": 6},
#     {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
#     {"city": "New York", "iataCode": "JFK", "lowestPrice": 240, "id": 8},
#     {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
#     {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
# ]

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
six_month_from_today = datetime.date.today() + datetime.timedelta(days=1 + 6 * 30)

ORIGIN_CITY_IATA = "GRU"

pp = pprint.PrettyPrinter(indent=4)

# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flightSearch.get_iata_code(row["city"])
#     dataManager.destination_data = sheet_data
#     dataManager.post_sheety_data()

print(sheet_data)

for destionation in sheet_data:
    flight = flightSearch.get_cheap_flights(
        ORIGIN_CITY_IATA,
        destionation["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today  
    ) 