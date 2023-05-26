import googlemaps

class Searching_module:
    #search_counter = 0
    # init method or constructor
    API_KEY = 'insert_api_key_here'

    def __init__(self, current_location = None):
        self.m_object_list = []
        if current_location:
            self.m_object_list[0] = current_location
    
    def convert_miles_to_meters (miles):
        try:
            return miles * 1_609.344
        except:
            return -1

    def get_m_object_list(self):
        return self.m_object_list
        
    def set_m_object_list(self,list):
        self.m_object_list = list

    def search_the_area(self):
        pass

    def remove_old_objects(self):
        self.m_object_list = []

    def start_searching_module(self, current_location):
        if (current_location == ()):
            return -2
        elif (-90 < current_location[0] < 90 or -180 < current_location[1] < 180):
            return -1
        else:
            return 0

    def start_searching_module(self, input_location = None, input_radius = None):
        map_client = googlemaps.Client(API_KEY)
        if (input_location):
            response = map_client.places_nearby (location = input_location, radius = input_radius)

    def prepare_search_result (self, params):
        pass

        
        
#test with request, worth to try gmaps won't work well
#import requests

# set up the API endpoint and parameters
#url = "https://maps.googleapis.com/maps/api/place/radarsearch/json"
#params = {
    #"location": "50.060683036581125,19.935779508513296", # latitude,longitude of the center of the search area
    #"radius": 5000, # search radius in meters
    #"type": "restaurant", # type of place to search for
    #"key": "" # replace with your own API key
#}

# send the request and get the response
#response = requests.get(url, params=params)
#print(response)
#data = response.json()

# extract the place_ids
# place_ids = [result["place_id"] for result in data["results"]]
# while "next_page_token" in data:
#     params["pagetoken"] = data["next_page_token"]
#     response = requests.get(url, params=params)
#     data = response.json()
#     place_ids += [result["place_id"] for result in data["results"]]
