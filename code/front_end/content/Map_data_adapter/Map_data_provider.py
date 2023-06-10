import time

"""
DP: Wzorzec Adapter (Adapter pattern): Map_place_provider jest używany do transformacji interfejsu jednej klasy, 
takiej jak searching module na interfejs oczekiwany przez inne obiekty. 

Klasa Map_place_provider wykorzystuje metody back_endu, takie jak provide_places(), get_time() i outside_area(). 
W metodzie download_places() pobierane są miejsca z back_endu i zapisywane w atrybucie klasy. 
Metoda ta jest również wywoływana co 5 minut oraz gdy użytkownik opuszcza obszar wyszukiwania.
Metoda get_places() jest zaprojektowana tak, aby zwracać tylko te miejsca, które nie były wcześniej zwracane.
"""

# DG - dotyczy diagramów
# DG: self.object swap on self.places
class Map_place_provider:
    def __init__(self, backend_module: object):
        # DG object swap on places and getter and setter
        self.places_raw = []

        self.map_info = {}
        self.date = ""
        self.data_status = 0
        self.timer = 5
        self.receiving_time = []

        ### INITIALIZATION ###
        ## 10.06.23 Here is searching module
        self.backend_module = backend_module


    def download_places(self):
        # print(self.backend_module, hasattr(self.backend_module, 'provide_objects'))
        if self.backend_module is None:
            return -1
        # if hasattr(self.backend_module, 'provide_objects') == 0:
        #     return -1
        # places = self.arr_module.provide_objects()
        places = [
            {
                "id": 334234,
                "name": "a Grande Mamma",
                "category": "Restaurant",
                "lat": 33.88,
                "lon": -84.42,
                "description": "Good place",
                ## Rating: (rating, how much people rate)
                "rating": (4.2, 60)
            },
            {
                "id": 43243,
                "name": "Aparthotel Stare Miasto",
                "category": None,
                "lat": 33.85,
                "lon": -84.42,
                "description": None,
                "rating": None
            },
            {
                "id":1,
                "name": "Hello1",
                "category":None,
                "desription":None,
                "rating": (4,50),
                "lat": 33.75,
                "lon": -84.41
            },
            {
                "id":2,
                "name": "Hello2",
                "category":None,
                "desription":None,
                "rating": (4,50),
                "lat": 33.75,
                "lon": -84.43
            },
            {
                "id":3,
                "name": "Hello3",
                "category":None,
                "desription":None,
                "rating": (4,50),
                "lat": 33.80,
                "lon": -84.45
            },
            {
                "id": 4,
                "name": "Hello3",
                "category": None,
                "desription": None,
                "rating": (4, 50),
                "lat": 35,
                "lon": -84.45
            },
        ]

        ### wojtek7z -> added this section to try get real places from openstreet map,
        ### each time to download places, use get_search_result method invoked on object 
        ### of type 'Searching_module', in the final version of the app, it shouldn't be called
        ### directly, but only after check_proximity method was called 
        ### so method to call in cycles would be 'start_location_module', invoked ON CLASS 
        ### directly, and Location_module would check if proximity condition is still met
        places = self.backend_module.get_search_result()
        print(places)

        # END OF THE SECTION
        ###########################################

        if len(places) == 0:
            return -2

        u_time = int(time.time())
        self.receiving_time.append(u_time)
        self.places_raw = places
        self.data_status = 1

        return 0

    # DG: get_objects swap on get_places
    def get_places_raw(self):
        return self.places_raw
    def get_map_info(self): pass
    def get_data_status(self): pass
    def get_date(self): pass
    def get_timer(self):
        return self.timer

    def set_places(self): pass
    def set_map_info(self): pass
    def set_data_status(self): pass
    def set_date(self): pass
    def set_timer(self):
        pass
