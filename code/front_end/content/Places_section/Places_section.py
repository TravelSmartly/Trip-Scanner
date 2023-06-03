from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock

from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
import os

class Place_option(MDBoxLayout):
    description = StringProperty("")
    rating = StringProperty("")
    def __init__(self, description, rating, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.rating = rating

"""
Rozdział listy pobiera dane o obiektach i wyświetla ich w formie listy
"""
class Places_section(Screen):
    navigation_manager = ObjectProperty(None)
    navigation_manager_go_to_previous = ObjectProperty(None)
    places = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = MDApp.get_running_app()
        map_adp = app.map_data_adapter
        self.map_adp = map_adp

        self.places = self.map_adp.get_places()

        Clock.schedule_once(self.show_content)
    def show_content(self, dt):
        ## Zeby mozna bylo sie cofnac i dzialal przycisk Back
        self.navigation_manager_go_to_previous = self.navigation_manager.go_to_previous_tab

        for place in self.places:
            if "description" not in place:
                place["description"] = None
            description = "Description: "+ str(place["description"])
            rating = "Rating: " + str(place["rating"])
            self.ids.box.add_widget(
                MDExpansionPanel(
                    icon=os.path.join(images_path, "logo", "kivymd-icon-128.png"),
                    content=Place_option(description, rating),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=str(place["name"]),
                        secondary_text="{0},{1}".format(place["lat"],place["lon"]),
                        tertiary_text=str(place["category"])
                    )
                )
            )

    def open_desription(self): pass
    def request_places(self): pass