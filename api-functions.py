import os
import requests

API_KEY = os.environ['API_KEY']

def get_place_coordinates(place):
    """Requests & returns coordinates from OpenTripMap for a place"""

    url = f'https://api.opentripmap.com/0.1/en/places/geoname?name={place}&apikey={API_KEY}'

    req = requests.get(url)

    place_data = req.json()

    return place_data

    