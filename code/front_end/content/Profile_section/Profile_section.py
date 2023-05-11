from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, OneLineListItem, OneLineAvatarIconListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import StringProperty, OptionProperty
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.clock import Clock
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine


class MyContent(BoxLayout):
    pass


"""
Profile section służy do wyboru kategorii dla poszczególnych profilów.
Równiez mozna wybrac sam profil
"""
class Profile_section(Screen):
    def __init__(self, **kwargs):
        super(Profile_section, self).__init__(**kwargs)
        Clock.schedule_once(self.show_content)


    profiles = ()

    categories = ()

    sub_categories = ()

    curr_profile = ""

    def show_content(self, dt):
        print("hi")
        names = ["Opiton1", "Option2", "Option3"]

        for name in names:
            panel = MDExpansionPanel(
                panel_cls=MDExpansionPanelOneLine(
                    text=name
                ),
                icon="",
                content=MyContent())
            self.ids.panel_container.add_widget(panel)

    def show_distance_range(sefl): pass
    def extract_categories(sefl): pass
    def extract_profile(sefl): pass
    def send_categories(sefl): pass
    def seve_categories(sefl): pass

    def get_categories(sefl): pass
    def set_categories(sefl): pass



class Profile_category(BoxLayout):
    active = 0
    changed = 0
    category_info = []
    def category_processing(self): pass
    def get_active(self): pass
    def get_changed(self): pass
    def get_category_info(self): pass

    def set_active(self): pass

    def set_changed(self): pass
    def set_category_info(self): pass
