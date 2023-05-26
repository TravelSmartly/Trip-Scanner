from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineAvatarListItem, OneLineListItem, TwoLineListItem, MDList
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty

class Map_description_content(MDScrollView):
    pass

#
#
class Map_description:
    menu = None
    map_section = ObjectProperty(None)

    def __init__(self, market_data):
        super().__init__()

        headers = {
            "Name": [market_data["name"], 1],
            "Lat": [market_data["lat"],1],
            "Lon": [market_data["lon"],1]
        }
        # print(market_data)
        content = Map_description_content()
        list = MDList()
        content.add_widget(list)
        for [k, v] in headers.items():
            new_widget = None
            if v[1] == 2:
                new_widget = TwoLineListItem(text=f"{k}:", secondary_text=f"{v[0]}")
            else:
                new_widget = OneLineListItem(text=f"{k}: {v[0]}")
            list.add_widget(
                new_widget
            )

        self.menu = MDDialog(
            title="Place description",
            type="custom",

            content_cls=content
        )


    def get_menu(self):
        return self.menu

    link: str
    imgs: list
    favorite: int

    def is_it_favorite(self): pass

    def get_url(self): pass

    def get_img(self): pass

    def set_img(self): pass

    def set_url(self): pass
