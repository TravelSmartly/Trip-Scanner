# from content.Providers.Map_place_provider import Map_place_provider
# from back_end.arranging_module import Arranging_module
# import unittest
import time


class Map_place_provider:
    def __init__(self, arranging_module):
        # DG object swap on places and getter and setter
        self.places = []
        # self.places = [
        #     {
        #         "id": 334234,
        #         "name": "a Grande Mamma",
        #         "category": None,
        #         "coordinates": (50.06163905474776, 19.936530642326513),
        #         "description": None,
        #         "rating": None
        #     },
        #     {
        #         "id": 43243,
        #         "name": "Aparthotel Stare Miasto",
        #         "category": None,
        #         "coordinates": (50.06182501735149, 19.933510474939244),
        #         "description": None,
        #         "rating": (4.2, 60)
        #     }
        # ]

        self.map_info = {}
        self.date = ""
        self.data_status = 0
        self.timer = 0

        ### INITIALIZATION ###
        self.arr_module = None
        if isinstance(arranging_module, object):
            self.arr_module = arranging_module


    def download_places(self):
        if self.arr_module is None:
            return -1
        if hasattr(self.arr_module, 'provide_objects') == 0:
            return -1
        places = self.arr_module.provide_objects()

        if len(places) != 0:
            u_time = int(time.time())
            for place in places:
                place.download_time = u_time
            self.places = places
            self.data_status = 1
        else:
            return -2

        return 0

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
    def __init__(self, arranging_module):
        # DG: data swaped on places_data razem z get i set, type from dict swaped on list
        self.places_data = []

        ### INITIALIZATION ###
        super().__init__(arranging_module)

    def data_postprocessing(self):
        is_dl = self.download_places()
        if is_dl == -1:
            return -1
        places = self.get_places()
        self.places_data.append(places)

    def test_favorite_processing(self): pass
    def get_places_data(self):
        return self.places_data

    def set_places_data(self): pass