from content.Providers.Map_place_provider import Map_place_provider
from back_end.arranging_module import Arranging_module
import unittest

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