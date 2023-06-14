#import googlemaps
import overpy
import math
import json
from .location_module import *


class Searching_module:
    #search_counter = 0
    API_KEY = 'insert_api_key_here'
    config_module = None

    def __init__(self, current_location = None):
        self.m_object_list = []
        #if current_location:
        #    self.m_object_list[0] = current_location
        #else:
        #    self.m_object_list[0] = (-999, -999)


    def set_config_module(self, config_module):
        self.config_module = config_module
    
    def convert_miles_to_meters (self, miles):
        try:
            return miles * 1_609.344
        except:
            return -1

    def distance_between_two_latlon (self, lat_lon1, lat_lon2):
        try:
            return math.sqrt ( pow (lat_lon1[0] * 111320 - lat_lon2[1] * 111320, 2) + 
            pow ( (40075000 * math.cos(lat_lon1[1]) / 360) - (40075000 * math.cos(lat_lon2[1]) / 360), 2) )  
        except:
            return -1
            


    def get_m_object_list(self):
        return self.m_object_list
        
    def set_m_object_list(self,my_list):
        self.m_object_list = my_list

    def remove_old_objects(self):
        self.m_object_list.clear()

    #def start_searching_module(self, input_location = None, input_radius = None):
    #    map_client = googlemaps.Client(API_KEY)
    #   if -90 > input_location[0] > 90 or 180 < input_location[1] < -180:
    #        return -1
    #    if input_location:
    #        response = map_client.places_nearby (location = input_location, radius = input_radius)
    #    else:
    #        return -2

    def search_the_area(self,coordinates, radius, category, subcategory):
        lat, lon = coordinates[0], coordinates[1]
        api = overpy.Overpass()
        
        #lat, lon = 50.05918219735402, 20.003032346862184 # Kraków
        #radius = 2000  # w metrach
        #category = "amenity"
        #subcategory = "restaurant"  # typ miejsca
        #print (f"category : {category}")
        # ~ print (f"subcategory : {subcategory}")

        # ~ # Zapytanie Overpass do znalezienia typów miejsc w określonym promieniu
        # ~ query = f"""
        # ~ [out:json];
        # ~ (
            # ~ node["{category}"="{subcategory}"](around:{radius},{lat},{lon});
            # ~ way["{category}"="{subcategory}"](around:{radius},{lat},{lon});
        # ~ );
        # ~ out center;
        # ~ """
        
        query = f"""
        [out:json];
        (
            node[{category}](around:{radius},{lat},{lon});
        );
        out center;
        """

        result = api.query(query)
        # ~ print (result.nodes)

        # Wyświetl nazwy i lokalizacje znalezionych miejsc
        for idd, element in enumerate(result.nodes):
            #print(f"Name: {element.tags.get('name', 'unknown')}, Location: {element.lat}, {element.lon}")
            object_location = (float(element.lat), float(element.lon))
            subj_distance = self.distance_between_two_latlon (object_location, coordinates)
            object_a = {
                'id': (idd + 1),
                'name': element.tags.get('name', 'unknown'), 
                'category': category,
                'lat': float (element.lat),
                'lon': float (element.lon),
                'description': 'a place just for you!',
                'rating': 'no rating',
                'distance': subj_distance
            }
            if object_a['name'] != 'unknown':
                self.m_object_list.append (object_a)
            # ~ print (object_a)

        # ~ for element in result.ways:
            # ~ #print(f"Name: {element.tags.get('name', 'unknown')}, Location: {element.center_lat}, {element.center_lon}")
            # ~ object_location = (element.lat, element.lon)
            # ~ subj_distance = self.distance_between_two_latlon (object_location, coordinates)
            # ~ object_a = {
                # ~ 'id': idd,
                # ~ 'name': element.tags.get('name', 'unknown'), 
                # ~ 'category': subcategory,
                # ~ 'lat': element.lat,
                # ~ 'lon': element.lon,
                # ~ 'description': 'a place just for you!',
                # ~ 'rating': 'no rating',
                # ~ 'distance': subj_distance
            # ~ }
            # ~ self.m_object_list.append (object_a)
            # ~ idd += 1

        return self.m_object_list

    def get_search_result (self):
        config_module = self.config_module
        if config_module is None:
            return []
        if self.m_object_list != [] and Location_module.check_proximity(int(self.config_module.proximity), Location_module.current_location, Location_module.center_location):
            return self.m_object_list

        self.remove_old_objects()

        category_dictionaries = config_module.get_categories_dicts()
        #category_dictonaries contains keys such as: id, category, subcategories (list)
        # ~ print (category_dictionaries) 
        config_module.find_current_profile()
        #current_profile = json.loads (config_module.put_selected_profile_to_front())
        current_profile = config_module.put_selected_profile_to_front() 
        #current profile is a dict, with key 'categories' containing values (id-s) of all selected categories
        # ~ print (current_profile)
        selected_categories_list = current_profile["categories"]
        # ~ print (selected_categories_list)
        
        chosen_category_dicts = [category_dict for category_dict in category_dictionaries if int(category_dict["id"]) in selected_categories_list]
        for c_dict in chosen_category_dicts:
            subcategory_list = c_dict["subcategories"]
            # ~ print (subcategory_list[0])
            big_string = ",".join(subcategory_list)
            self.search_the_area (Location_module.get_current_location(), int(config_module.proximity), c_dict["category"], big_string)
            # ~ for each_sub in subcategory_list:
                # ~ print (each_sub)
                # ~ self.search_the_area (Location_module.get_current_location(), config_module.proximity, c_dict["category"], each_sub)
        
        # ~ print (self.m_object_list)
        return self.m_object_list