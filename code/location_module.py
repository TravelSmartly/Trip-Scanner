from kivy.app import App
from kivy.uix.label import Label
from plyer import gps
import pytest

class Location_module(App):
    lat = 3223
    lon = 34432
    center_location = []
    s_string:str
    3234432
    #type hints

    @staticmethod
    def get_current_location()->int:
        return 0
    def check_proximity(r,current_location,center_location)->bool:
        #zwraca true jesli current_location jest w srodku elipsy o srodku w punkcie center_location
        return (current_location[0]-center_location[0] * lat)^2 + (current_location[1]-center_location[1] * lon * cos(lat))^2 < (r)^2






    def put_user_location_front():
        pass

    def start_location_module(r,center_location):
        current_location = Location_module.get_current_location()
        searcher = None
        if not (Location_module.check_proximity(r,current_location,center_location)):#is outside of region
            #center_location = current_location
            #odpal searching module
            searcher = searching_module.Searching_module(current_location)
            try:
               searcher.start_seaching_module()
               return searcher
            except TypeError:
                print("Searcher for some reason didn't get initialised properly...")
                return -2
        return 0









    #unittests

    from unittest.mock import MagicMock
    from my_app import Localisation_module









