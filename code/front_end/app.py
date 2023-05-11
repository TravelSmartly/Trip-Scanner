###- IMPORT KIVY -###
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.animation import Animation
from kivymd.uix.expansionpanel import MDExpansionPanel

###- END IMPORT KIVY -###

import os
from sys import path as sys_path
import time
import sqlite3


###- IMPORT NAJWAZNIESZYCH KOMPONENTOW -###
from .content.Map_section.__init__ import *
from .content.Places_section.__init__ import *
from .content.Profile_section.__init__ import *
from .content.Section_header.__init__ import *
from .content.Nav_bar.Nav_bar import *
from .content.test.test import *
###- END IMPORT NAJWAZNIESZYCH KOMPONENTOW -###


## To jest najwazniejsza klassa, ktora odpowiada za przelaczenie rozdzialow
class WindowManager(ScreenManager):
    previous_object = StringProperty("map_section")

## Absolute import app.kv
kv_path = os.path.join(os.path.dirname(__file__), 'app.kv')
kv = Builder.load_file(kv_path)
#kv = Builder.load_file("front_end/app.kv")

def chk_conn(conn):
    try:
        conn.cursor()
        return True
    except Exception as ex:
        return False

## W tym miejscu zaczyna sie caly graficzny interfejsc
class FrontApp(MDApp):
    connection = None
    cursor = None
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"

        self.connection = sqlite3.connect("markets.db")
        if chk_conn(self.connection):
            self.cursor = self.connection.cursor()

        self.sm = WindowManager()
        return self.sm



FrontApp().run()
