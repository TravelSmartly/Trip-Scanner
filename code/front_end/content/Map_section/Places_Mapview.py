from kivymd.app import MDApp
from .mapview_build.lib.kivy_garden.mapview import MapView
from .Map_object import Map_object
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
"""
DG: w diagramach jest po prostu Mapview, zamieniłem na Places_Mapview, żeby nie wyglądało podobnie do MapView
Map view zarządza obiektem mapa. Zadaniem Mapview jest rozstawienie miejsc i lokalizacji użytkownika tam,
gdzie to powinno być. I  później odświeżać te dane.
"""
class Places_Mapview(MapView):
    min_max_lat_lon: list
    getting_place_timer = None
    places_names: list
    places = ListProperty(0)
    specific_place: dict
    # DG: added location
    location = {"lat": 33.75, "lon": -84.4}
    places_id = set()

    def __init__(self, **krawgs):
        super(Places_Mapview, self).__init__(**krawgs)
        app = MDApp.get_running_app()
        map_adp = app.map_data_adapter
        self.map_adp = map_adp

        self.places = self.map_adp.get_places()
        timer = self.map_adp.get_timer()

        Clock.schedule_interval(self.refresh_places, timer)





    def show_map_place(self): pass


    def start_getting_place_in_fov(self):
        # After one second, get the places in the field of view
        try:
            self.getting_place_timer.cancel()
        except:
            pass

        self.getting_place_timer = Clock.schedule_once(self.get_place_in_fov, 0.5)


    def get_place_in_fov(self,  *args):
        # Get reference to main app and the database cursor
        # print(self.get_bbox())
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        # app = MDApp.get_running_app()
        # print(app)
        # sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s " % (
        # min_lon, max_lon, min_lat, max_lat)
        #
        # app.cursor.execute(sql_statement)
        # markets = app.cursor.fetchall()
        places = self.places
        # print(places)
        for place in places:
            place_id = place["id"]
            lat, lon = place["lat"], place["lon"]
            if place_id in self.places_id:
                continue
            # print(place)
            if min_lat < lat and lat < max_lat and min_lon < lon and lon < max_lon:
                self.add_places(place)
            # self.add_places(place)


    def add_places(self, place):
        lat, lon = place["lat"], place["lon"]
        # print(lat, lon)
        marker = Map_object(lat=lat, lon=lon)
        marker.place_data = place
        self.add_widget(marker)

        # Keep track of the marker's name
        place_id = place["id"]
        self.places_id.update([place_id])
        # print(self.places_id)

    # DG: funkcje add_localization wykonuje gpshelper, ktory ciagle aktualizuje lokalizacje
    # def add_localization(self):



    ## Again a download new place
    def refresh_places(self, dt):
        self.map_adp.postprocessing()
        # print(self.places)


    def refresh_localization(self): pass


    def select_specific_place(self): pass
