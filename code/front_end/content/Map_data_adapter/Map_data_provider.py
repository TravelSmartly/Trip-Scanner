import time

"""
Klasa Map_place_provider wykorzystuje metody back_endu, takie jak provide_places(), get_time() i outside_area(). 
W metodzie download_places() pobierane są miejsca z back_endu i zapisywane w atrybucie klasy. 
Metoda ta jest również wywoływana co 5 minut oraz gdy użytkownik opuszcza obszar wyszukiwania.
Metoda get_places() jest zaprojektowana tak, aby zwracać tylko te miejsca, które nie były wcześniej zwracane.
"""

# DG - dotyczy diagramów
# DG: self.object swap on self.places
class Map_place_provider:
    def __init__(self, arranging_module: object):
        # DG object swap on places and getter and setter
        self.places_raw = []

        self.map_info = {}
        self.date = ""
        self.data_status = 0
        self.timer = 5
        self.receiving_time = []

        ### INITIALIZATION ###
        self.arrg_module = arranging_module


    def download_places(self):
        # print(self.arrg_module, hasattr(self.arrg_module, 'provide_objects'))
        if self.arrg_module is None:
            return -1
        # if hasattr(self.arrg_module, 'provide_objects') == 0:
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
