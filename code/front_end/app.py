from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
import os
from sys import path as sys_path
import time

from .content.Map_section.__init__ import *
from .content.Places_section.__init__ import *
from .content.Profile_section.__init__ import *
from .content.Section_header.__init__ import *
from .content.Nav_bar.Nav_bar import *


# if __name__ != "__main__":
#     exit()

class WindowManager(ScreenManager):
	pass

class Content_manager():
    pass

# Absolute import app.kv
kv_path = os.path.join(os.path.dirname(__file__), 'app.kv')
kv = Builder.load_file(kv_path)
#kv = Builder.load_file("front_end/app.kv")

class FrontApp(MDApp):
    def build(self):
        self.sm = WindowManager()
        return self.sm

FrontApp().run()
