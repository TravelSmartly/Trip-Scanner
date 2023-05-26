class Searching_module:
    #search_counter = 0
    # init method or constructor
    def __init__(self, current_location = None):
        self.m_object_list = []
        if current_location:
            self.m_object_list[0] = current_location



    def get_m_object_list(self):
        return self.m_object_list
    def set_m_object_list(self,list):
        self.m_object_list = list
    def search_the_area(self):
        pass
    def remove_old_objects(self):
        pass
    def start_searching_module(self, current_location):
        if (current_location == ()):
            return -2
        elif (-90 < current_location[0] < 90 or -180 < current_location[1] < 180):
            return -1
        else:
            return 0
        
        
#test with request, worth to try gmaps won't work well
import requests

# set up the API endpoint and parameters
url = "https://maps.googleapis.com/maps/api/place/radarsearch/json"
params = {
    "location": "50.060683036581125,19.935779508513296", # latitude,longitude of the center of the search area
    "radius": 5000, # search radius in meters
    "type": "restaurant", # type of place to search for
    "key": "" # replace with your own API key
}

# send the request and get the response
response = requests.get(url, params=params)
print(response)
#data = response.json()

# extract the place_ids
# place_ids = [result["place_id"] for result in data["results"]]
# while "next_page_token" in data:
#     params["pagetoken"] = data["next_page_token"]
#     response = requests.get(url, params=params)
#     data = response.json()
#     place_ids += [result["place_id"] for result in data["results"]]
