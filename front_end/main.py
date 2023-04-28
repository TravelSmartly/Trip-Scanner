# from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp

import unittest
from content.Map_section.Map_section import *

if __name__ != "__main__":
    exit()


class WindowManager(ScreenManager):
    pass



class Content_manager():
    pass



# kv = Builder.load_file("main.kv")


class FrontApp(MDApp):
    def build(self):
        return 0

#arranging_module = Arranging_module()

#FrontApp().run()
unittest.main()
