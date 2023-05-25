from kivy.garden.mapview import MapView
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock

"""
Rozdział listy pobiera dane o obiektach i wyświetla ich w formie listy
"""
class Places_section(Screen):
    navigation_manager = ObjectProperty(None)
    navigation_manager_go_to_previous = ObjectProperty(None)
    places = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.show_content)
    def show_content(self, dt):
        self.navigation_manager_go_to_previous = self.navigation_manager.go_to_previous_tab

    def open_desription(self): pass
    def request_places(self): pass