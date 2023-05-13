from kivy.uix.widget import Widget
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.button import MDTextButton
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, OptionProperty, ObjectProperty

from kivy.clock import Clock


class Section_header_right_button(Label):
    button_text = StringProperty("")
    def do_transition(self): pass


## Header, odpowiada za pokazanie rozdziału i rownież zarządzanie przyciskami na górze
class Section_header(Screen):
    ## Referencja na prawy przycisk
    r_but_obj = ObjectProperty(None)

    header_text = StringProperty("<")
    r_but_options = {"None": Section_header_right_button,
                     "Set_profile": None }
    r_but_option = StringProperty("None")
    is_header_displayed = 0


    def __init__(self, **kwargs):
        super(Section_header, self).__init__(**kwargs)
        ## To odpala mozliwosc wyboru przycisku
        # Clock.schedule_once(self.show_custom_right_button_option)
        ## To pozwala dodac kastomowy przycisk do prawej czesci headera
        Clock.schedule_once(self.show_custom_right_button)


    def show_custom_right_button(self, dt):
        right_button_obj = None
        if self.r_but_obj is not None:
            right_button_obj = self.r_but_obj
        else:
            right_button_obj = Section_header_right_button()
        self.ids.right_button.add_widget(right_button_obj)

    def show_custom_right_button_option(self, dt):
        right_button_obj = None
        for option in self.r_but_options:
            if option == self.r_but_option:
                right_button_obj = self.r_but_options[option]()
        self.ids.right_button.add_widget(right_button_obj)

    def show_header(self):
        pass

class Section_header_return_button(MDTextButton):
    but_text = StringProperty("Back")
    def get_last_section(self): pass
    def return_to_last_section(self):
        # print(dir(MDApp.get_running_app().root))
        MDApp.get_running_app().root.current = MDApp.get_running_app().root.previous_object
        # app.transition.direction = 'left'
        # self.current = self.previous()


