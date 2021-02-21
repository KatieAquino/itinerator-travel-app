import os
import requests

API_KEY = os.environ['API_KEY']

def get_place_coordinates(place):
    """Requests & returns coordinates from OpenTripMap for a place"""

    url = f'https://api.opentripmap.com/0.1/en/places/geoname?name={place}&apikey={API_KEY}'

    req = requests.get(url)

    place_data = req.json()

    return place_data


def get_points_of_interests(place_data, radius=20000, kinds=None):
    """Requests & returns points of interests for given location,
    defaults to a radius of 48280 meters, roughly 30 miles"""

    lon = place_data['lon']
    lat = place_data['lat']
    mult_categories = []
    final_req = []

    #will return all categories
    if kinds == None:
        url = f'https://api.opentripmap.com/0.1/en/places/radius?radius={radius}&lon={lon}&lat={lat}&format=json&limit=20&apikey={API_KEY}'
        req = requests.get(url)

        return req.json()

    #loops through kinds to make individual request per category
    #returns list of json elements
    else:
        for item in kinds:
            req = requests.get(f'https://api.opentripmap.com/0.1/en/places/radius?radius={radius}&lon={lon}&lat={lat}&kinds={item}&format=json&limit=20&apikey={API_KEY}')
            req = req.json()
            mult_categories.append(req)
        
        for category in mult_categories:
            for element in category:
                final_req.append(element)
        
        return final_req


def get_place_info(place_list):
    """Takes list of places and returns detailed information for each place"""

    place_details = []

    for place in place_list:
        place_id = place['xid']

        url = f'https://api.opentripmap.com/0.1/en/places/xid/{place_id}?apikey={API_KEY}'
        req = requests.get(url)
        req = req.json()

        if 'wikipedia' in req and 'preview' in req:

            place_details.append({'name': req['name'], 
                                'wikipedia': req['wikipedia'], 
                                'image': req['preview']['source'],
                                'extract': req['wikipedia_extracts']['text']})

    return place_details

