from kivy.uix.widget import Widget
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class Section_header(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    header_text = StringProperty("Hello")
    is_header_displayed = 0
    def hi(self):
        print("hello")
    def show_header(self):
        pass

class Section_header_return_button(Button):
    def get_last_section(self): pass
    def return_to_last_section(self):
        # print(dir(MDApp.get_running_app().root))
        MDApp.get_running_app().root.current = MDApp.get_running_app().root.previous_object
        # app.transition.direction = 'left'
        # self.current = self.previous()


class Section_header_right_button(Button):
    pass