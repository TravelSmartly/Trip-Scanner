# from content.Providers.Map_place_provider import Map_place_provider
# from back_end.arranging_module import Arranging_module
# import unittest


class Map_place_provider:
    def __init__(self, location_module):
        # DG self.object swap on self.places
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


    def test_download_places(self):
        self.places = self.arranging_module.provide_objects()

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





class Map_data_adapter(Map_place_provider):
    def setUp(self):

        self.data = {

        }

    def test_data_postprocessing(self):
        self.test_download_places()
        places = self.get_places()

    def test_favorite_processing(self): pass
    def get_data(self): pass

    def set_data(self): pass