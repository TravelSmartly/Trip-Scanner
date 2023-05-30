import unittest
from back_end.location_module import Location_module
# DG - dotyczy diagramów

# DG self.object swap on self.places
class Map_place_provider:
    def __init__(self, location_module):
        # Set fixed existing objects
        self.places = [
            {
                "id": 334234,
                "name": "a Grande Mamma",
                "category": None,
                "coordinates": (50.06163905474776, 19.936530642326513),
                "description": None,
                "rating": None
            },
            {
                "id": 43243,
                "name": "Aparthotel Stare Miasto",
                "category": None,
                "coordinates": (50.06182501735149, 19.933510474939244),
                "description": None,
                "rating": (4.2, 60)
            }
        ]

        self.map_info = {}
        self.date = ""
        self.data_status = 0
        self.timer = 0

        self.assertTrue(hasattr(Location_module, 'provide_objects'))
        self.arranging_module = Location_module()


    def download_places(self):
        self.assertEqual(self.arranging_module.provide_objects(), self.places)

    # DG: get_objects swap on get_places
    def get_places(self):
        return self.places
    def get_map_info(self): pass
    def get_data_status(self): pass
    def get_date(self): pass
    def get_timer(self): pass

    def set_places(self): pass
    def set_map_info(self): pass
    def set_data_status(self): pass
    def set_date(self): pass
    def set_timer(self): pass