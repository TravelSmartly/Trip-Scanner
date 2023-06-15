from kivymd.app import MDApp
from .mapview_build.lib.kivy_garden.mapview import MapView, MapLayer
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
    location = {"lat": 50.05918219735402, "lon": 20.003032346862184}
    places_id = set()
    markers = []
    places_memory = []
    layer = ObjectProperty(None)

    app = ObjectProperty(None)
    places_section = ObjectProperty(None)


    def __init__(self, **krawgs):
        super(Places_Mapview, self).__init__(**krawgs)
        self.app = MDApp.get_running_app()
        map_adp = self.app.map_data_adapter
        self.map_adp = map_adp

        self.places = self.map_adp.get_places()
        timer = self.map_adp.get_timer()

        Clock.schedule_once(self.start_conf)
        self.refresh_places(0)
        Clock.schedule_interval(self.refresh_places, timer)
        ## Sprawdzam, czy nie wyszedlem poza obszar
        # Clock.schedule_interval(self.check_outside_area, 5)
        # self.layer = MapLayer()
        # self.add_layer(self.layer)
        self.x = 0

    def start_conf(self, dt):
        self.places_section = self.app.places_section

    def show_map_place(self): pass


    def check_outside_area(self, dt):
        is_outside_area = self.map_adp.outside_area()
        if is_outside_area == 0:
            self.refresh_places(1)


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
        # for place in places:
        #     print(place)
        # print(self.x ,"XD\n\n\n")
        # self.x+=1
        # print(places)
        # print(self.places_memory)
        for place in places:
            place_id = place["id"]
            lat, lon = place["lat"], place["lon"]
            if place not in self.places_memory:
                if min_lat <= lat and lat <= max_lat and min_lon <= lon and lon <= max_lon:
                    ## !!! W tym miejscu dodaje takze miejsca do listy
                    self.add_places(place)
                    self.put_place_to_places_list(place)

            # self.add_places(place)


    def put_place_to_places_list(self, place):
        self.places_section.add_place_to_list(place)


    def add_places(self, place):
        # print(place)
        lat, lon = place["lat"], place["lon"]
        # print(lat, lon)
        marker = Map_object(lat=lat, lon=lon)
        marker.set_place_data(place)
        self.add_marker(marker)
        self.markers.append(marker)
        # print(marker, place)
        # print(marker.place_id)

        # Keep track of the marker's name
        self.places_memory.append(place)

    # DG: funkcje add_localization wykonuje gpshelper, ktory ciagle aktualizuje lokalizacje
    # def add_localization(self):

    def remove_markers_out_of_screen(self):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        for marker_obj in self.markers:
            marker = marker_obj.get_place_data()
            lat, lon = marker["lat"], marker["lon"]
            # print(min_lat, max_lat, min_lon, max_lon, " OK ", lat, lon)
            if (min_lat > lat or lat > max_lat) or (min_lon > lon or lon > max_lon):
                self.remove_marker_object(marker_obj)


                    # self.places_id.remove(marker["id"])
                    # self.markers.remove(marker_obj)
                    # self.remove_widget(marker_obj)


    def remove_marker_object(self,marker):
        m_data = marker.get_place_data()
        self.places_memory.remove(m_data)
        self.markers.remove(marker)
        # self.remove_widget(marker)
        self.remove_marker(marker)
        return 0


    def remove_all_markers(self):
        # print("REMOVING")
        # print("START\n\n")
        # marker_layout = self.children[0].chils
        for marker_obj in self.markers:
            # print(marker_obj)
            self.remove_marker_object(marker_obj)

        # self.places_memory.clear()
        # self.markers.clear()
        # print("after REMOVING\n\n\n")
        # print(self.markers)


    ## Again a download new place
    def refresh_places(self, dt):
        # print(dt)
        ## Pobieram dane z back-endu
        self.map_adp.postprocessing()
        self.places = self.map_adp.get_places()
        ## Wyczyszczam wszystkie stare obiekty poza obszarem
        ## dt jet 0, jesli to pierwsza inicjalizacja
        if dt != 0:
            self.remove_markers_out_of_screen()
        ## Odswierzam obiekty na mpie w poblizu
        # self.start_getting_place_in_fov()
        # print(self.places)


    def refresh_localization(self): pass


    def select_specific_place(self): pass
