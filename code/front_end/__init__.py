from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
import os
from sys import path as sys_path
from front_end.content.Map_section.__init__ import *
from front_end.content.Nav_bar.Nav_bar import *
import time

# if __name__ != "__main__":
#     exit()


class WindowManager(ScreenManager):
    pass



class Content_manager():
    pass

print("EFWEF")
print(os.path.dirname(__file__), os.path.join(os.path.dirname(__file__), '__init__.kv'))
kv_path = os.path.join(os.path.dirname(__file__), '__init__.kv')
kv = Builder.load_file(kv_path)
#kv = Builder.load_file("front_end/__init__.kv")

class FrontApp(MDApp):
    def build(self):
        return kv

FrontApp().run()
