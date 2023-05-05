from kivy.uix.widget import Widget
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class Section_header(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_set_profile_button()

    header_text = StringProperty("Hello")
    is_header_displayed = 0
    def hi(self):
        print("hello")

    def show_set_profile_button(self):
        right_button_obj = Section_header_right_button()
        # print(self.ids.right_button)
        # self.ids.right_button.add_widget(right_button_obj)

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
    profile_text=StringProperty("")
    pass

# Przeniesc pozniej do Profile_section
class Section_header_set_profile_button(Section_header_right_button):
    profile_text="SetProfile"