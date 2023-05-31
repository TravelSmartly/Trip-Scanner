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

    def __init__(self, place_data):
        super().__init__()
        if "description" not in place_data:
            place_data["description"] = None

        if "category" not in place_data:
            place_data["category"] = None

        if "rating" not in place_data:
            place_data["rating"] = None

        coords = "({0},{1})".format(place_data["lat"], place_data["lon"])
        headers = {
            "Name": [1, place_data["name"]],
            "Coordinates": [1, coords],
            "Category": [1, place_data["category"]],
            "Description": [2, place_data["description"]],
            "Rating": [2, place_data["rating"]],
        }
        # print(place_data)
        content = Map_description_content()
        list = MDList()
        content.add_widget(list)
        for [k, v] in headers.items():
            new_widget = None
            if v[0] == 2:
                new_widget = TwoLineListItem(text=f"{k}:", secondary_text=f"{v[1]}")
            else:
                new_widget = OneLineListItem(text=f"{k}: {v[1]}")
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
