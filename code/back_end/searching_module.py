#import googlemaps
import overpy
import math

class Searching_module:
    #search_counter = 0
    API_KEY = 'insert_api_key_here'

    def __init__(self, current_location = None):
        self.m_object_list = []
        #if current_location:
        #    self.m_object_list[0] = current_location
        #else:
        #    self.m_object_list[0] = (-999, -999)
    
    def convert_miles_to_meters (miles):
        try:
            return miles * 1_609.344
        except:
            return -1

    def distance_between_two_latlon (lat_lon1, lat_lon2):
        try:
            return math.sqrt ( pow (lat_lon1[0] * 111320 - lat_lon2[1] * 111320, 2) + 
            pow ( (40075000 * math.cos(lat_lon1[1]) / 360) - (40075000 * math.cos(lat_lon2[1]) / 360), 2) )  
        except:
            return -1
            


    def get_m_object_list(self):
        return self.m_object_list
        
    def set_m_object_list(self,list):
        self.m_object_list = list

    def remove_old_objects(self):
        self.m_object_list = []

    #def start_searching_module(self, input_location = None, input_radius = None):
    #    map_client = googlemaps.Client(API_KEY)
    #   if -90 > input_location[0] > 90 or 180 < input_location[1] < -180:
    #        return -1
    #    if input_location:
    #        response = map_client.places_nearby (location = input_location, radius = input_radius)
    #    else:
    #        return -2

    def search_the_area(coordinates, radius, category, subcategory):
        lat, lon = coordinates[0], coordinates[1]
        api = overpy.Overpass()
        
        #lat, lon = 50.05918219735402, 20.003032346862184 # Kraków
        #radius = 2000  # w metrach
        #category = "amenity"
        #subcategory = "restaurant"  # typ miejsca

        # Zapytanie Overpass do znalezienia typów miejsc w określonym promieniu
        query = f"""
        [out:json];
        (
            node["{category}"="{subcategory}"](around:{radius},{lat},{lon});
            way["{category}"="{subcategory}"](around:{radius},{lat},{lon});
        );
        out center;
        """

        result = api.query(query)

        # Wyświetl nazwy i lokalizacje znalezionych miejsc
        idd = 1
        for element in result.nodes:
            #print(f"Name: {element.tags.get('name', 'unknown')}, Location: {element.lat}, {element.lon}")
            object_location = (element.lat, element.lon)
            subj_distance = distance_between_two_latlon (object_location, coordinates)
            object_a = {
                'id': idd,
                'name': element.tags.get('name', 'unknown'), 
                'category': subcategory,
                'lat': element.lat,
                'lon': element.lon,
                'description': 'a place just for you!',
                'rating': 'no rating',
                'distance': subj_distance
            }
            self.m_object_list.append (object_a)
            idd += 1

        for element in result.ways:
            #print(f"Name: {element.tags.get('name', 'unknown')}, Location: {element.center_lat}, {element.center_lon}")
            object_location = (element.lat, element.lon)
            subj_distance = distance_between_two_latlon (object_location, coordinates)
            object_a = {
                'id': idd,
                'name': element.tags.get('name', 'unknown'), 
                'category': subcategory,
                'lat': element.lat,
                'lon': element.lon,
                'description': 'a place just for you!',
                'rating': 'no rating',
                'distance': subj_distance
            }
            self.m_object_list.append (object_a)
            idd += 1

        return self.m_object_list

    def get_search_result (self, config_module):
        category_dictionaries = config_module.get_categories_dicts()
        config_module.find_current_profile()
        #current_profile = json.loads (config_module.put_selected_profile_to_front())
        current_profile = config_module.put_selected_profile_to_front()
        selected_categories_list = current_profile["categories"]
        for category in selected_categories_list:
            for category_dict in category_dictionaries:
                if category_dict["category"] == category:
                    subcategory_list = category_dict["subcategories"]
                    for each_sub in subcategory_list:
                        search_the_area (Location_module.get_current_location(), config_module.proximity, category, each_sub)
        return self.m_object_list





        
