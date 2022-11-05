import requests
import datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

from config import TEQUILA_ENDPOINT, TEQUILA_QUERY, HEADER, TEQUILA_SEARCH
from flight_data import FlightData

# sheet_data = [
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
tomorrow_plus_6_months = datetime.date.today() + datetime.timedelta(days=1 + 6 * 30)


class FlightSearch:
    def get_iata_code(self, cityList: list):
        iata_codes_sheety = []
        for n in range(len(cityList)):
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}{TEQUILA_QUERY}",
                headers=HEADER,
                params={"term": {cityList[n]}, "location_types": "airport"},
            )
            data = response.json()["locations"][0]["code"]
            iata_codes_sheety.append(data)
        return iata_codes_sheety

    def get_cheap_flights(self, sheet_data: dict):
        
        
        for n in range(len(sheet_data)):
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}{TEQUILA_SEARCH}",
                headers=HEADER,
                params={
                    "fly_from": "GIG",
                    "fly_to": sheet_data[n]["iataCode"],
                    "max_stopovers": 2,
                    "date_from": tomorrow.strftime("%d/%m/%Y"),
                    "date_to": tomorrow_plus_6_months.strftime("%d/%m/%Y"),
                    "nights_in_dst_from": 7,
                    "nights_in_dst_to": 28,
                    "curr": "BRL",
                    "sort": "price",
                    "limit": 1,
                },
            )

