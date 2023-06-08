# from content.Providers.Map_place_provider import Map_place_provider
# from back_end.arranging_module import Arranging_module
# import unittest
from .Map_data_provider import Map_place_provider


class Map_data_adapter(Map_place_provider):
    def __init__(self, arranging_module):
        # DG: data swaped on places_data razem z get i set, type from dict swaped on list
        self.places = []
        self.sent_places = set()


        ### INITIALIZATION ###
        super().__init__(arranging_module)

    ## DG: Name changed from data_postprocessing on postprocessing
    def postprocessing(self):
        is_dl = self.download_places()
        if is_dl != 0:
            return -1
        self.places = self.get_places_raw()



    def test_favorite_processing(self): pass
    def get_places_unique(self):
        to_send_places = [place for place in self.places if place['id'] not in self.sent_places]
        self.sent_places.update([place['id'] for place in to_send_places])
        return to_send_places

    def get_places(self):
        return self.places

    def set_places_data(self): pass