from kivy.app import App
from kivymd.app import MDApp

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import MDList, OneLineListItem, OneLineAvatarIconListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty, OptionProperty
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.clock import Clock
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine
from kivymd.uix.button import MDTextButton

from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.checkbox import CheckBox


class Profile_manager(ScreenManager):
    navigation_manager = ObjectProperty(None)
    previous_tab_name = StringProperty("map_section")
    def go_to_previous_tab(self):
        self.transition.direction = 'left'
        try:
            self.current = self.previous_tab_name
        except:
            pass
            # print("NO")


class Section_header_set_profile_button(MDTextButton):
    profile_manager = ObjectProperty(None)
    button_text = "Set profile"


## RightCheckbox odpowiada za wybor kategorii, jesli uzytkownik wprowadzil zmiany,
## to, wyswietla sie przycisk aby ta kategoria sie zapisala
class RightCheckbox(IRightBodyTouch, MDCheckbox):
    root_id = NumericProperty(0)
    root_text = StringProperty("")
    profile_section = ObjectProperty(None)
    ##- PROFILE ADAPTER -##
    profile_mnp = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile_mnp = MDApp.get_running_app().profile_manipulator

    def on_press(self, *args):
        is_active = self.active  ## or args[1]

        if is_active:
            ## Jesjli uzytkownik wybral kategorie, wylij to do manipulatora
            self.profile_mnp.select_category(self.root_id)
            is_changed = self.profile_mnp.get_change_status()
            if is_changed == 1:
                self.profile_section.show_save_layout()
            else:
                self.profile_section.hide_save_layout()
                # self.profile_section.add_widget(self.profile_section.ids.save_layout)
            # else:
            #     self.profile_section.remove_widget(self.profile_section.ids.save_layout)
            # print("active")
            # print(self.root_id)
            # print(self.root_text)
        else:
            self.profile_mnp.deselect_category(self.root_id)
            is_changed = self.profile_mnp.get_change_status()
            if is_changed == 1:
                self.profile_section.show_save_layout()
            else:
                self.profile_section.hide_save_layout()
            # print("DISABLE")
            # print(self.root_id)
            # print(self.root_text)



class MyContent(BoxLayout):
    pass



class Profile_category(OneLineAvatarIconListItem):
    category_id = NumericProperty(0)

    is_active = BooleanProperty(False)
    profile_section = ObjectProperty(None)
    changed = 0
    category_info = []

    icon = StringProperty("android")

    def __init__(self, category_id, active, profile_section, **kwargs):
        super().__init__(**kwargs)
        self.category_id = category_id
        self.is_active = active
        self. profile_section = profile_section


    def on_open(self):
        print(self)


    def category_processing(self): pass


    def get_active(self): pass
    def get_changed(self): pass
    def get_category_info(self): pass

    def get_check_box(self):
        return self.ids.my_check_box

    def set_active(self): pass
    def set_changed(self): pass
    def set_category_info(self): pass



"""
Profile section służy do wyboru kategorii dla poszczególnych profilów.
Równiez mozna wybrac sam profil
"""
class Profile_section(Screen):
    navigation_manager = ObjectProperty(None)
    navigation_manager_go_to_previous = ObjectProperty(None)
    profile_manager = ObjectProperty(None)
    r_but = ObjectProperty(None)
    app = None

    profiles = []
    categories = []
    sub_categories = ()
    curr_profile = ""
    ## DG: ilosc kategorii
    cat_len = 0
    ## DG: current index relative to ScrollView postion
    ## Dynamicznie pokazuje kategorie
    curr_i = 0
    curr_i_end = cat_len
    i_increasing = 5
    first_increase = True
    getting_cat_timer = None

    ## DG: selected profile, it referes to selected profile
    selected_profile = None
    selected_profile_name = StringProperty("")
    selected_categories = []

    ## DG: selected boxes will help me to reselect these boxes
    check_boxes = []

    def hi(self):
        print("HI PROFILE SECTTION")

    def __init__(self, **kwargs):
        super(Profile_section, self).__init__(**kwargs)
        ## r_but is for passing it into Section header, to show "Set profile" on the top right
        self.r_but = Section_header_set_profile_button()

        ##- PROFILE ADAPTER -##
        app = MDApp.get_running_app()
        profile_mnp = app.profile_manipulator
        category_adp = app.category_adapter
        self.profile_mnp = profile_mnp
        self.category_adt = category_adp

        self.categories = category_adp.get_categories()
        self.categories_inst = category_adp.get_instraction()
        self.curr_i_end = len(self.categories)

        self.profiles = profile_mnp.get_profiles()
        self.profile_inst = profile_mnp.get_instraction()
        self.selected_profile = profile_mnp.get_selected()
        # print(self.selected_profile, "selected_profile")

        self.selected_categories = self.selected_profile[self.profile_inst["categories"]]
        self.selected_profile_name = self.selected_profile[self.profile_inst["name"]]
        # print(self.selected_profile_name)
        ##- END OF PROFILE ADAPTER -##

        ## To ma za zadanie wyświetlić content po ladowaniu aplikacji, nie mozna tego robic w init
        ## poniewaz w show_content UYWAM ids! To jest bardzo wazne, poniewaz w init ids jeszcze nie sa
        ## znalezione, wiec nalezy poczekac, poki sie pojawia, wiec Clock czeka chwile i pokazuje kontent
        ## Mozliwe, ze sie da zrobic to inaczej, ale nie umiem
        Clock.schedule_once(self.show_content)

    def show_content(self, dt):
        self.r_but.profile_manager = self.profile_manager
        self.navigation_manager_go_to_previous = self.navigation_manager.go_to_previous_tab
        # print(self.navigation_manager_go_to_previous)

        icons = list(md_icons.keys())
        first_cat = None
        cat_name = self.categories_inst["name"] ## category
        cat_icon = self.categories_inst["icon"] ## icon
        cat_id = self.categories_inst["id"] ## id
        for i in range(self.curr_i, self.curr_i_end):
            category = self.categories[i]
            is_active = False
            # print(self.selected_categories, cat_id)
            if category[cat_id] in self.selected_categories:
                is_active = True
            category_widget = Profile_category(
                text=category[cat_name],
                active=is_active,
                icon=icons[category[cat_icon]],
                category_id=category[cat_id],
                profile_section=self
            )
            check_box = category_widget.get_check_box()
            self.check_boxes.append(check_box)
            if i == self.curr_i:
                first_cat = category_widget
            self.ids.panel_container.add_widget(category_widget)
        return first_cat


    def reselect(self):
        for check_box in self.check_boxes:
            # check_box.active = True
            if check_box.root_id in self.selected_categories:
                check_box.active = True
                # print(check_box.root_text)

            # print(check_box)


    def show_save_layout(self):
        save_layout = self.ids.save_layout
        # print(self.ids.save_layout)
        save_layout.size_hint = (1, 0.15)
        save_layout.height = 30
        save_layout.opacity = 1

    def hide_save_layout(self):
        save_layout = self.ids.save_layout
        save_layout.size_hint = (None, None)
        save_layout.height = 0
        save_layout.opacity = 0

    def send_profile(self):
        did_send_correctly = self.profile_mnp.prepare_send_profile()
        if did_send_correctly != 0:
            pass
        self.hide_save_layout()
        # self.reselect()


    ## DG: Added dinamic scrolled, which  is missing on deagrams, but this is additional
    ##- Dinamic scroll -##
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
            self.curr_i = self.curr_i_end
            self.curr_i_end += self.i_increasing
            if self.curr_i_end > self.cat_len:
                self.curr_i_end = self.cat_len
            first_cat = self.show_content(None)
            # self.ids.my_scroll_view.scroll_to(first_cat)

    ##- END OF Dinamic scroll -##

    def show_distance_range(self): pass

    def extract_categories(sefl): pass

    def extract_profile(sefl): pass

    def send_categories(sefl): pass

    def seve_categories(sefl): pass

    def get_categories(sefl): pass

    def set_categories(sefl): pass
