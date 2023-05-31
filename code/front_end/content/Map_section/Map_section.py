from kivymd.app import MDApp
# from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
import os
from .Places_Mapview import Places_Mapview
from .gpsblinker import GpsBlinker
# from .Map_description import Map_description

"""
Map_section sluzy do wyswietlenia rodzialu mapu
Map seciton 
Rozdział mapy, tutaj wyświetlam wszystkie miejsca na mapie zgodnie z kategoriami, które starannie pobraliśmy z innych serwisów. 
Drugie założenie jest takie, że to właśnie Map_section ma za zadanie pobrać dane o miejscach z adaptera i przekazać je do Mapview

Klassa Map_section POWINNA dziedziczyc Screen, poniewaz jest w klasie
WindowManager
WindowManager, zarzadza Screen'ami
"""
class Map_section(Screen):
    navigation_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Map_section, self).__init__(**kwargs)

        ### MAP DATA ADAPTER
        # app = MDApp.get_running_app()
        # map_adp = app.map_data_adapter
        # self.map_adp = map_adp

    def show_map(self):
        pass
    def show_map_error(self): pass
    def show_objects(self, dt):
        pass
        # self.places = self.map_adp.get_places_unique()
        # print(self.places)
    def show_help(self): pass



class Map_object_button():
    description_status: int

    def show_description(self): pass
    def hide_description(self): pass
    def reset_description(self): pass






class Map_description_button():
    hiding_percentage: int

    def press(self): pass


class Map_favorite_button():
    is_favorite: int
    def remove_from_favorite(self): pass

    def add_to_favorite(self): pass
