# from kivy.garden.mapview import MapMarkerPopup
from .mapview_build.lib.kivy_garden.mapview import MapMarker
from .Map_description import Map_description
import os

"""
Map_object to jest marker miejsca, czyli ikona, ktora pokazuje, gdzie znajduje sie miejsce
"""
class Map_object(MapMarker):
    # cordX: int
    # cordY: int
    # cord: int
    # id: int
    # display_status: int
    # from_place_list: int
    place_data = []
    place_id = -1
    menu = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        src = os.path.join(os.path.dirname(__file__), 'marker.png')
        self.source = src
    # market_data = []


    def on_release(self):
        # Open up the LocationPopupMenu
        if not self.menu:
            self.menu = Map_description(self.place_data)
            # print("hello")
        menu = self.menu.get_menu()
        menu.open()

    def getCord(self): pass
    def getStatus(self): pass

    def get_place_data(self):
        return self.place_data

    ## DG: dodalem ustwienie i pobieranie place data
    def set_place_data(self, place):
        self.place_data = place
        self.place_id = place["id"]

    def setCord(self): pass
    def setStatus(self): pass
