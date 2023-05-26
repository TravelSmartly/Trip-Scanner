from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.garden.mapview import MapView
# from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import os
from .Map_object import Map_object
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
    # def __init__(self):
    #     super().__init__()
        # GpsBlinker()

    def show_map(self):
        print("hi")
    def test_show_map_error(self): pass
    def test_show_objects(self): pass
    def test_show_help(self): pass



""" 
DG: w diagramach jest po prostu Mapview, zamieniłem na Places_Mapview, żeby nie wyglądało podobnie do MapView
Map view zarządza obiektem mapa. Zadaniem Mapview jest rozstawienie miejsc i lokalizacji użytkownika tam, 
gdzie to powinno być. I  później odświeżać te dane.
"""
class Places_Mapview(MapView):
    min_max_lat_lon: list
    getting_place_timer = None
    places_names: list
    places: list
    specific_place: dict
    # DG: added location
    location = {"lat":33.75, "lon": -84.4}
    market_names = []

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
        # print(self.get_bbox())
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = MDApp.get_running_app()
        # print(app)
        # sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s " % (
        # min_lon, max_lon, min_lat, max_lat)
        #
        # app.cursor.execute(sql_statement)
        # markets = app.cursor.fetchall()
        places = [
            {
                "name": "Hello",
                "lat": 33.879017,
                "lon": -84.12754
            },
            {"name": "Hello1", "lat":33.75, "lon": -84.41},
            {"name": "Hello2", "lat":33.75, "lon": -84.43},
            {"name": "Hello3", "lat":33.75, "lon": -84.45},
            {"name": "Hello4", "lat":33.75, "lon": -84.60},
            {"name": "Hello5", "lat":33.75, "lon": -84.70},
            {"name": "Hello6", "lat":33.75, "lon": -85.20},
            {"name": "Hello7", "lat":33.90, "lon": -85.40},
            {"name": "Hello8", "lat":33.80, "lon": -85.20},
            {"name": "Hello9", "lat":33.76, "lon":-84.181030},
            {"name": "Hello10", "lat":33.77, "lon":-84.181030},
            {"name": "Hello11", "lat":33.78, "lon":-84.181030}
        ]
        # print(places)
        for place in places:
            name = place["name"]
            if name in self.market_names:
                continue
            else:
                self.add_places(place)
            # self.add_places(place)


    def add_places(self, place):
        lat, lon = place["lat"], place["lon"]
        # print(lat, lon)
        marker = Map_object(lat=lat, lon=lon)
        marker.place_data = place
        self.add_widget(marker)

        # Keep track of the marker's name
        name = place["name"]
        self.market_names.append(name)


    # DG: literówka w add_localizasion, zamienione na add_localization
    def add_localization(self):
        lat, lon = self.location["lat"], self.location["lon"]
        location = Map_object(lat=lat, lon=lon)
        self.add_widget(location)



    def refresh_places(self): pass


    def refresh_localization(self): pass


    def select_specific_place(self): pass



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
