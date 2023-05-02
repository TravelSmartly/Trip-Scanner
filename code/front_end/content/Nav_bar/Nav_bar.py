from kivy.uix.widget import Widget

### Nav_bar jest przyciskami pod
class Nav_bar(Widget):
    def __init__(self, **kwargs):
        super(Nav_bar, self).__init__(**kwargs)
        self.is_nav_bar_displayed = ""
        self.last_section = ""
        self.curr_section = ""

    def show_nav_bar(self): pass
    def show_nav_bar_error(self): pass
    def nav_bar_status(self): pass

    def get_last_section(self): pass
    def get_curr_section(self): pass

    def set_last_section(self): pass

class Nav_bar_button(Widget):
    def change_color(self): pass
    def change_img(self): pass
    def change_section(self): pass