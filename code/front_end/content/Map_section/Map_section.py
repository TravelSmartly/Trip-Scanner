from kivymd.app import MDApp
# from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem, OneLineListItem, TwoLineListItem, MDList
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import os
from .Places_Mapview import Places_Mapview
from .gpsblinker import GpsBlinker
# from .Map_description import Map_description
class Help_popup_menu_content(MDScrollView):
    pass
class Help_popup_menu:
    menu = None
    map_section = ObjectProperty(None)

    def __init__(self, menu_data, title):
        # print(menu_data)
        content = Help_popup_menu_content()
        menu_list = MDList()
        content.add_widget(menu_list)
        for [k, v] in menu_data.items():
            new_widget = None
            if v[0] == 2:
                new_widget = TwoLineListItem(text=f"{k}:", secondary_text=f"{v[1]}")
            else:
                new_widget = OneLineListItem(text=f"{k}: {v[1]}")
            menu_list.add_widget(
                new_widget
            )

        self.menu = MDDialog(
            title=title,
            type="custom",
            content_cls=content
        )

    def get_menu(self):
        return self.menu

    link: str
    imgs: list
    favorite: int

    def is_it_favorite(self):
        pass

    def get_url(self):
        pass

    def get_img(self):
        pass

    def set_img(self):
        pass

    def set_url(self):
        pass

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
    help_popup = ObjectProperty(None)
    # help_information = {
    #     "places": "",
    #     "category": "ok",
    #     "description": "bruh",
    #     "rating": "XD"
    # }
    help_popup_headers = {
        "Maps": [2, "ergreigeri grg ero \ngreop gjerop geo pge ger gre ge"],
        "category": [1, "category"],
        "Description": [2, "description"],
        "Rating": [2, "rating"],
    }

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
    def show_help(self):
        if not self.help_popup:
            self.help_popup = Help_popup_menu(self.help_popup_headers, "Help menu")
            # print("hello")
        help_popup = self.help_popup.get_menu()
        help_popup.open()



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
