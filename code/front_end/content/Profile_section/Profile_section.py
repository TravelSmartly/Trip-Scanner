from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, OneLineListItem, OneLineAvatarIconListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import StringProperty, NumericProperty, OptionProperty
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.clock import Clock
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine

from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons



class MyContent(BoxLayout):
    pass


class Profile_category(OneLineAvatarIconListItem):

    def __init__(self, category_id, active, **kwargs):
        super().__init__(**kwargs)
        self.category_id = category_id
        self.active

    category_id = NumericProperty(0)

    active = 0
    changed = 0
    category_info = []

    icon = StringProperty("android")

    def on_open(self):
        print(self)

    def category_processing(self): pass

    def get_active(self): pass

    def get_changed(self): pass

    def get_category_info(self): pass

    def set_active(self): pass

    def set_changed(self): pass

    def set_category_info(self): pass


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    root_id = NumericProperty(0)
    root_text = StringProperty("")

    def on_active(self, *args):
        is_active = self.active  ## or args[1]
        if is_active:
            print(self.root_id)
            print(self.root_text)


"""
Profile section służy do wyboru kategorii dla poszczególnych profilów.
Równiez mozna wybrac sam profil
"""


class Profile_section(Screen):
    def __init__(self, **kwargs):
        super(Profile_section, self).__init__(**kwargs)
        Clock.schedule_once(self.show_content)

    profiles = [
        {
            "text":"profile0",
            "p_id": 0,
            "selected": 1,
            "categories": [0, 2, 3, 4]
        },
        {
            "text": "profile1",
            "p_id": 0,
            "selected": 1,
            "categories": [0, 1]
        }
    ]

    categories = (
        {
            "id": 0,
            "text": "Option0",

            "selected": 1
        },
        {
            "id": 1,
            "text": "Option1",
            "selected": 1
        },
        {
            "id": 2,
            "text": "Option2",
            "selected": 1
        },
        {
            "id": 3,
            "text": "Option3",
            "selected": 1
        },
        {
            "id": 4,
            "text": "Option4",
            "selected": 1
        },
        {
            "id": 5,
            "text": "Option5",
            "selected": 1
        }
    )

    sub_categories = ()

    curr_profile = ""

    ## DG: ilosc kategorii
    cat_len = len(categories)

    ## DG: current index relative to ScrollView postion
    ## Dynamicznie pokazuje kategorie
    curr_i = 0
    curr_i_end = cat_len
    i_increasing = 12
    first_increase = True
    getting_cat_timer = None

    def show_content(self, dt):
        icons = list(md_icons.keys())
        first_cat = None
        for i in range(self.curr_i, self.curr_i_end):
            category = Profile_category(text=f"Item {self.categories[i]}", active=True, icon=icons[i], category_id=i)
            if i == self.curr_i:
                first_cat = category
            self.ids.panel_container.add_widget(category)
        return first_cat


    def hi(self):
        print("HI")

    def scroll_event(self, x, y):
        # print(x, y)
        if (y < 0.05):
            try:
                self.getting_cat_timer.cancel()
            except:
                pass
            self.getting_cat_timer = Clock.schedule_once(self.increase_i, 0.1)


    def increase_i(self, dt):

        increasing = self.i_increasing
        if (self.curr_i_end < self.cat_len):
            # if self.first_increase:
            #     increasing = self.curr_i_end
            #     self.first_increase = False
            self.curr_i = self.curr_i_end
            self.curr_i_end += self.i_increasing
            if self.curr_i_end > self.cat_len:
                self.curr_i_end = self.cat_len
            first_cat = self.show_content(None)
            # print(first_cat.text)
            #
            # self.ids.my_scroll_view.scroll_to(first_cat)

    def show_distance_range(self): pass

    def extract_categories(sefl): pass

    def extract_profile(sefl): pass

    def send_categories(sefl): pass

    def seve_categories(sefl): pass

    def get_categories(sefl): pass

    def set_categories(sefl): pass
