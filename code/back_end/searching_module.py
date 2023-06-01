#import googlemaps
import overpy

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

    def start_searching_module(self, input_location = None, input_radius = None):
        map_client = googlemaps.Client(API_KEY)
        if -90 > input_location[0] > 90 or 180 < input_location[1] < -180:
            return -1
        if input_location:
            response = map_client.places_nearby (location = input_location, radius = input_radius)
        else:
            return -2

    def search_the_area(coordinates, radius, typ):
        lat, lon = coordinates[0], coordinates[1]
        api = overpy.Overpass()
        
        lat, lon = 50.05918219735402, 20.003032346862184 # Kraków
        radius = 2000  # w metrach
        typ = "restaurant"  # typ miejsca

        # Zapytanie Overpass do znalezienia typów miejsc w określonym promieniu
        query = f"""
        [out:json];
        (
            node["amenity"="{typ}"](around:{radius},{lat},{lon});
            way["amenity"="{typ}"](around:{radius},{lat},{lon});
            relation["amenity"="{typ}"](around:{radius},{lat},{lon});
        );
        out center;
        """

        result = api.query(query)
        print (result.nodes)

        # Wyświetl nazwy i lokalizacje znalezionych miejsc
        for element in result.nodes:
            print(f"Name: {element.tags.get('name', 'unknown')}, Location: {element.lat}, {element.lon}")

        for element in result.ways:
            print(f"Name: {element.tags.get('name', 'unknown')}, Location: {element.center_lat}, {element.center_lon}")

    def prepare_search_result (self, params):
        pass
