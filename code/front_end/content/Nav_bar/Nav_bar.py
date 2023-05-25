from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRoundFlatButton, MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.properties import StringProperty, BooleanProperty
from kivymd.app import MDApp
from kivy.clock import Clock
### Nav_bar jest przyciskami pod


class Navigation(MDBottomNavigation):
    previous_tab_name = StringProperty("map_section")
    def go_to_previous_tab(self):
        last_name = self.previous_tab_name
        self.switch_tab(last_name)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Clock.schedule_once(self.show_nav_bar, 1)

    def show_nav_bar(self, td):
        pass
        # self.switch_tab("profile_section")


class Nav_bar(Screen):
    section_name = StringProperty("")
    active = StringProperty("")
    def __init__(self, **kwargs):
        super(Nav_bar, self).__init__(**kwargs)
        self.is_nav_bar_displayed = ""
        self.last_section = ""
        self.curr_section = ""
        Clock.schedule_once(self.show_nav_bar, 0.01)

    def show_nav_bar(self, td):
        pass

    def show_nav_bar_error(self): pass
    def nav_bar_status(self): pass

    def get_last_section(self): pass
    def get_curr_section(self): pass

    def set_last_section(self): pass



## DG: Added Nav_bar_button_item to group button icon and text
class Nav_bar_button_item(MDFloatLayout):
    button_icon = StringProperty("")
    screen_name = StringProperty("")
    button_text = StringProperty("")
    active = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.show_nav_bar_button)

    def show_nav_bar_button(self, args):
        if self.active == True:
            self.ids.nav_bar_icon.icon_color = MDApp.get_running_app().theme_cls.primary_color
            self.ids.nav_bar_button.text_color = MDApp.get_running_app().theme_cls.primary_color
        # if self.active == True:



class Nav_bar_button_abstract:
    def change_color(self): pass
    def change_img(self): pass
    def change_section(self, section):
        app = MDApp.get_running_app().sm
        app.previous_object = app.current
        app.current = section
        app.transition.direction = "down"


class Nav_bar_button(MDRoundFlatButton, Nav_bar_button_abstract):
    screen_name = StringProperty("map_section")
    selected = BooleanProperty(False)



## DG: Added icon button
class Nav_bar_button_icon(MDIconButton, Nav_bar_button_abstract):
    screen_name = StringProperty("map_section")
