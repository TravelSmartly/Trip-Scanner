from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, OneLineListItem, OneLineAvatarIconListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import StringProperty, OptionProperty
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.clock import Clock
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine

from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons

class MyContent(BoxLayout):
    pass


class Profile_category(MDExpansionPanel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    active = 0
    changed = 0
    category_info = []

    def on_open(self):
        print(self.panel_cls.text)
        self.panel_cls.text = self.panel_cls.text + " +"
        self.open_icon = "front_end/icons/test/okpn.png"

    def category_processing(self): pass

    def get_active(self): pass

    def get_changed(self): pass

    def get_category_info(self): pass

    def set_active(self): pass

    def set_changed(self): pass

    def set_category_info(self): pass




class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


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
        print("HI")
        names = ["Opiton1", "Option2", "Option3"]
        icons = list(md_icons.keys())
        for i in range(30):
            panel = ListItemWithCheckbox(text=f"Item {i}", icon=icons[i])
            self.ids.panel_container.add_widget(panel)
        # for name in names:
            # panel = Profile_category(
            #     panel_cls=MDExpansionPanelOneLine(
            #         id="openLine",
            #         text=name
            #     ),
            #     icon="front_end/icons/test/lolp.png",
            #     content=MyContent()
            # )
            # self.ids.panel_container.add_widget(panel)

    def show_distance_range(self): pass

    def extract_categories(sefl): pass

    def extract_profile(sefl): pass

    def send_categories(sefl): pass

    def seve_categories(sefl): pass

    def get_categories(sefl): pass

    def set_categories(sefl): pass
