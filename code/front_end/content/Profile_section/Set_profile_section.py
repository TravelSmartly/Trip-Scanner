from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, OptionProperty, ObjectProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.boxlayout import BoxLayout

class RightCheckbox_profile(IRightBodyTouch, MDCheckbox):
    root_id = NumericProperty(0)
    root_text = StringProperty("")


    def on_press(self, *args):
        is_active = self.active  ## or args[1]
        if is_active:
            print("HI")
            print(self.root_id)
            print(self.root_text)



class MyContent(BoxLayout):
    pass



class Profile_profile(OneLineAvatarIconListItem):
    category_id = NumericProperty(0)

    is_active = BooleanProperty(False)
    changed = 0
    category_info = []

    icon = StringProperty("android")

    def __init__(self, profile_id, active, **kwargs):
        super().__init__(**kwargs)
        self.profile_id = profile_id
        self.is_active = active
        # print(self.profile_manager)


    def on_open(self):
        print(self)


    def category_processing(self): pass


    def get_active(self): pass
    def get_changed(self): pass
    def get_category_info(self): pass

    def set_active(self): pass
    def set_changed(self): pass
    def set_category_info(self): pass



class Set_profile_section(Screen):
    navigation_manager = ObjectProperty(None)
    profile_manager = ObjectProperty(None)
    profile_manager_go_to_previous = ObjectProperty(None)

    profiles = []
    ## DG: current index relative to ScrollView postion
    curr_i = 0
    curr_i_end = 0

    def __init__(self, **kwargs):
        super(Set_profile_section, self).__init__(**kwargs)

        ##- PROFILE ADAPTER -##
        app = MDApp.get_running_app()
        profile_mnp = app.profile_manipulator
        self.profile_mnp = profile_mnp



        self.profiles = profile_mnp.get_profiles()
        self.profile_inst = profile_mnp.get_instraction()
        self.selected_profile = profile_mnp.get_selected()
        self.curr_i_end = len(self.profiles)
        # print(self.selected_profile, "selected_profile w set_profile")

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
        self.profile_manager = MDApp.get_running_app().root.ids.nav_bar_id.ids.profile_manager_id
        self.profile_manager_go_to_previous = self.profile_manager.go_to_previous_tab
        prof_name = self.profile_inst["name"]  ## name
        prof_icon = self.profile_inst["icon"]  ## icon
        prof_id = self.profile_inst["id"]  ## id
        for i in range(self.curr_i, self.curr_i_end):
            # print(self.profiles[i])
            profile = self.profiles[i]
            is_active = False
            if profile[prof_name] == self.selected_profile[prof_name]:
                is_active = True
            profile_widget = Profile_profile(text=profile[prof_name], active=is_active, profile_id=i)
            self.ids.panel_container.add_widget(profile_widget)
        return 0
    def change_profiel(self): pass
    def remove_profile(self): pass
    def add_profile(self): pass

    def get_profiles(self): pass

    def set_profiles(self): pass
