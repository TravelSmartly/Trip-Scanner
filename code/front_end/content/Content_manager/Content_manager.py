from kivy.uix.screenmanager import Screen

class Content_manager(Screen):
    is_content_displayed = None
    is_nav_bar_displayed = None
    is_intarface_displayed = None
    last_section = None
    curr_section = None

    def show_content(self): pass
    def show_nav_bar(self): pass
    def content_status(self): pass
    def nav_bar_status(self): pass

    def get_last_section(self): pass

    def set_last_section(self): pass
