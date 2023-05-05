from kivy.app import App
from kivy.clock import Clock
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.screenmanager import Screen
import os

# from .Map_object import Map_object

class Map_object(MapMarkerPopup):
    # cordX: int
    # cordY: int
    # cord: int
    # id: int
    # display_status: int
    # from_place_list: int
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        src = os.path.join(os.path.dirname(__file__), 'marker.png')
        self.source = src
    # market_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        pass

    def getCord(self): pass
    def getStatus(self): pass

    def setCord(self): pass
    def setStatus(self): pass

class Map_section(Screen):
    def show_map(self):
        print("hi")
    def test_show_map_error(self): pass
    def test_show_objects(self): pass
    def test_show_help(self): pass


# DG: w diagramach po prostu Mapview, zamieniłem na Places_Mapview, żeby nie wyglądało podobnie do MapView
class Places_Mapview(MapView):
    min_max_lat_lon: list
    getting_place_timer = None
    places_names: list
    places: list
    specific_place: dict
    # DG: added location
    location = {"lat":33.75, "lon": -84.4}

    def show_map_place(self): pass


    def start_getting_place_in_fov(self):
        # After one second, get the places in the field of view
        try:
            self.getting_place_timer.cancel()
        except:
            pass

        self.getting_place_timer = Clock.schedule_once(self.get_place_in_fov, 1)


    def get_place_in_fov(self,  *args):
        # Get reference to main app and the database cursor
        print(self.get_bbox())
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        # print(app)
        # sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s " % (
        # min_lon, max_lon, min_lat, max_lat)
        #
        # app.cursor.execute(sql_statement)
        # markets = app.cursor.fetchall()
        places = [
            {"lat":33.879017, "lon": -84.12754},
            {"lat":33.75, "lon": -84.41},
            {"lat":33.75, "lon": -84.43},
            {"lat":33.75, "lon": -84.45},
            {"lat":33.75, "lon": -84.60},
            {"lat":33.75, "lon": -84.70},
            {"lat":33.75, "lon": -85.20},
            {"lat":33.90, "lon": -85.40},
            {"lat":33.80, "lon": -85.20},
            {"lat":33.76, "lon":-84.181030},
            {"lat":33.77, "lon":-84.181030},
            {"lat":33.78, "lon":-84.181030}
        ]
        print(places)
        for place in places:
            self.add_places(place)


    def add_places(self, place):
        lat, lon = place["lat"], place["lon"]
        # print(lat, lon)
        marker = Map_object(lat=lat, lon=lon)
        self.add_widget(marker)


    # DG: literówka w add_localizasion, zamienione na add_localization
    def add_localization(self):
        lat, lon = self.location["lat"], self.location["lon"]
        location = Map_object(lat=lat, lon=lon)
        self.add_widget(location)


    def refresh_places(self): pass


    def refresh_localization(self): pass


    def select_specific_place(self): pass



class Map_object_button(Map_object):
    description_status: int

    def show_description(self): pass
    def hide_description(self): pass
    def reset_description(self): pass



class Map_description():
    link: str
    imgs: list
    favorite: int

    def is_it_favorite(self): pass

    def get_url(self): pass
    def get_img(self): pass

    def set_img(self): pass
    def set_url(self): pass


class Map_description_button():
    hiding_percentage: int

    def press(self): pass


class Map_favorite_button():
    is_favorite: int
    def remove_from_favorite(self): pass

    def add_to_favorite(self): pass
