from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
import os
from sys import path as sys_path
from .content.Map_section.__init__ import *
from .content.Nav_bar.Nav_bar import *
import time

# if __name__ != "__main__":
#     exit()
Map_section().show_map()
class Lol(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

class Content_manager():
    pass

# Absolute import app.kv
kv_path = os.path.join(os.path.dirname(__file__), 'app.kv')
kv = Builder.load_file(kv_path)
#kv = Builder.load_file("front_end/app.kv")

class FrontApp(App):
    def build(self):
        return kv

FrontApp().run()
