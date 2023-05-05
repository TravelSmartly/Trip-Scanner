from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.boxlayout import BoxLayout
#from kivymd.uix.screenmanager import MDScreenManager


"""
Profile section służy do wyboru kategorii dla poszczególnych profilów.
Równiez mozna wybrac sam profil
"""
class Profile_section(Screen):
    profiles = ()

    categories = ()

    sub_categories = ()

    curr_profile = ""
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
