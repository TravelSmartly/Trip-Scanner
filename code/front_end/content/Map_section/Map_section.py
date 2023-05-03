#from Section_intarface import Section_intarface
from kivy.garden.mapview import MapView
from kivy.uix.screenmanager import Screen


class Map_section(Screen):
    def show_map(self):
        print("hi")
    def test_show_map_error(self): pass
    def test_show_objects(self): pass
    def test_show_help(self): pass


class Map_object():
    cordX: int
    cordY: int
    cord: int
    id: int
    display_status: int
    from_place_list: int

    def getCord(self): pass
    def getStatus(self): pass

    def setCord(self): pass
    def setStatus(self): pass

# DG: w diagramach po prostu Mapview, zamieniłem na Places_Mapview, żeby nie wyglądało podobnie do MapView
class Places_Mapview(MapView):
    getting_markets_timer = None


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
