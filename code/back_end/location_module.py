from kivy.app import App
from kivy.uix.label import Label
from plyer import gps
import pytest

class Location_module():
    lat = 111045 #one degree of latitude is always 69 miles = 111045 meters
    lon = 111045 #one degree of latitude in equator, sea level is 69 miles = 111045 meters
    center_location = []
    #s_string:str
    #type hints

    @staticmethod
    def on_gps_location(**kwargs)->None:
        #kwargs["lat"]=10.0
        #kwargs["lon"]=10.0
        print(kwargs)

    @staticmethod
    def get_current_location()->int:
        try:
            gps.configure(on_location=Location_module.on_gps_location)
            gps.start(2000)
            #coordinates = gps.
            return 0
        except Exception as e:
            return -1
    def check_proximity(r,current_location,center_location)->bool:
        #zwraca true jesli current_location jest w srodku elipsy o srodku w punkcie center_location
        return (current_location[0]-center_location[0] * Location_module.lat)^2 + (current_location[1]-center_location[1] * Location_module.lon * math.cos((current_location[0]+center_location[0])/2))^2 < (r)^2






    def put_user_location_front():

        tmp = Location_module.get_current_location()
        if tmp == -1:
            print("gps not work")
        return tmp
        #give coordinated for current or center location

    def start_location_module(r,center_location):
        current_location = Location_module.get_current_location()
        searcher = None
        if not (Location_module.check_proximity(r,current_location,center_location)):#is outside of region
            #center_location = current_location
            #odpal searching module
            Location_module.center_location = current_location
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









