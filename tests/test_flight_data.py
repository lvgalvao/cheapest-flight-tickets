import requests

import sys
sys.path.append("./app")

from app.config import SHEETY_PRICES_ENDPOINT
from app.flight_data import FlightData

information_data = {
                        "price":, 
                        "origin_cit"y=, 
                        "origin_airport"=,
                        "destination_city"=,
                        "destination_airport"=,
                        "out_date"=,
                        "return_date"= 
}
flightdata = FlightData(
                        price=, 
                        origin_city=, 
                        origin_airport=,
                        destination_city=,
                        destination_airport=,
                        out_date=,
                        return_date= 
                        )

# is API working?
# is API get what we need?
# is the function working?

# is the schema Flightdata working?

def check_schema_flightdata():
    flightdata = FlightData(information_data)
    assert "price" in flightdata
