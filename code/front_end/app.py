###- IMPORT KIVY -###
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager

###- END IMPORT KIVY -###

import os
from sys import path as sys_path
import time
import sqlite3


###- IMPORT NAJWAZNIESZYCH KOMPONENTOW -###
from .content.Map_section.gpshelper import GpsHelper
from .content.Map_section.__init__ import *
from .content.Places_section.__init__ import *
from .content.Profile_section.__init__ import *
from .content.Section_header.__init__ import *
from .content.Nav_bar.Nav_bar import *
from .content.test.test import *

from .content.Profile_adapter.Profile_adapter import Profile_manipulator, Category_adapter
from .content.Map_data_adapter.Map_data_adapter import Map_data_adapter
###- END IMPORT NAJWAZNIESZYCH KOMPONENTOW -###

from kivy.utils import platform
## Powidomienia
if platform == 'android':
    pass

from plyer import notification
import threading


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

""" 
DP: FrontApp używa Wzorca Fasady, dlatego, że, FrontApp, przyjmuje aż 4 obiekty z back-endu 
i działa na tych obiektach przekazując te obiekty innym obiektom 
A aby uruchomić tę aplikację wystarczy użyć metody build
DP: FrontApp używa Wzorca Singleton, ponieważ istnieje tylko jedna instancja FrontApp, w sumie tak samo jak
i inne rozdziały (sekcje), takie jak Map_Section, Profile_Section i td.
"""

## W tym miejscu zaczyna sie caly graficzny interfejsc
class FrontApp(MDApp):
    connection = None
    cursor = None
    conf_module = None
    loc_module = None
    search_module = None

    places_section = ObjectProperty(None)
    map_section = ObjectProperty(None)

    notification_go = 0


    def build(self):

        ###- ADAPTERTS -###
        ## DG: The profile adapter needs to be connected to Profile_section and Set_profile_section,
        ## but I decided to create it in the App Builder
        ## because otherwise I would have to create 2 profile adapters in Profile_section and Set_profile_section
        ## which is not good, and also I would have to import the adapter twice.
        self.profile_manipulator = Profile_manipulator(self.conf_module)
        self.profile_manipulator.postprocessing()
        self.category_adapter = Category_adapter(self.conf_module)
        self.category_adapter.postprocessing()

        self.map_data_adapter = Map_data_adapter(self.search_module)
        self.map_data_adapter.postprocessing()


        ###- END OF ADAPTERS -###

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        # self.theme_cls.primary_dark = ""
        self.theme_cls.disabled_button_primary_color = (89/255, 98/255, 104/255)

        self.connection = sqlite3.connect("markets.db")
        if chk_conn(self.connection):
            self.cursor = self.connection.cursor()

        self.sm = WindowManager()
        return self.sm


    def letsgo(self):
        print(self.notification_go)
        if self.notification_go == 1:
            return
        self.notification_go = 1
        self.background_thread = threading.Thread(target=self.printer.print_place)
        self.background_thread.start()

    def dontgo(self):
        if self.notification_go == 1:
            self.printer.stop()
            self.notification_go = 0



    def on_start(self):
        self.places_section = self.root.ids.nav_bar_id.ids.places_section_id
        self.map_section = self.root.ids.nav_bar_id.ids.map_section_id.ids.mapview

        # self.root.ids.bottom_navigation.switch_tab('screen 3')
        self.gpshelper = GpsHelper(self.map_section)
        self.gpshelper.run()

        class HelloWorldPrinter:
            def __init__(self, searcher):
                self.stop_printing = threading.Event()
                self.searcher = searcher


            def print_place(self):
                while not self.stop_printing.is_set():
                    print('Background!')
                    search_module = self.searcher
                    result = search_module.get_search_result()
                    last_result = {"name": "Null", "distance":"Null"}
                    if (len(result) != 0):
                        last_result = result[len(result)-1]
                        min_dist = result[0]["distance"]
                        min_name = result[0]["name"]
                        for place in result:
                            if place["distance"] < min_dist:
                                min_dist = place["distance"]
                                min_name = place["name"]

                        notification.notify(
                            title=min_name,
                            message=str(min_dist) + "m - Cool place",
                            timeout=2
                        )
                    time.sleep(20)

            def stop(self):
                self.stop_printing.set()

        self.printer = HelloWorldPrinter(self.search_module)
        self.letsgo()



    def set_conf_module(self, conf_module: object):
        self.conf_module = conf_module

    def set_location_module(self, loc_module: object):
        self.loc_module = loc_module

    def set_arranging_module (self, arrg_module: object):
        self.arrg_module = arrg_module

    def set_search_module(self, search_module: object):
        self.search_module = search_module

    def get_map_section(self):
        # print(self.map_section)
        return self.map_section

    def get_location_module(self):
        return self.loc_module

    # def on_pause(self):
    #     print("HELLO")
    #     return True
    #
    # def on_resume(self):
    #     print("RESUME")

    def on_stop(self):
        self.dontgo()
        print("HELLO STOP")

    # def set_gpshelper(self, gpshelper):
    #     self.gpshelper = gpshelper




