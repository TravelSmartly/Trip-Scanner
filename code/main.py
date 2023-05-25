### libraries
import os
import json
import pathlib
from time import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from plyer import gps
from plyer import notification

###-- BACK-END ZONE --###

###---- IMPORT BACK-END AND PACKAGES ----###
from back_end.__init__ import *

###---- END OF IMPORT BACK-END AND PACKAGES ----###


###-- END OF BACK-END ZONE --###



###-- FRONT-END ZONE --###
###---- IMPORT FRONT-END AND PACKAGES ----###
"""
Importuję w tym przypadku front_end/__init__.py
"""
from front_end.__init__ import *
###---- END OF IMPORT FRONT-END AND PACKAGES ----###

Window.size = (360, 640)

###-- END OF FRONT-END ZONE --###



###-- !!!START MAIN ZONE!!! --###

## DG: ! We changed name "main" to "MainApp"!
class MainApp:
    def __init__(self):
        print("hi")
    def on_stop(self):
        print("HELLO STOP")
    def start(self):
        ###-- BACK-END PART --###
        config_module = Configuration_module()
        config_module.read_profiles()
        config_module.read_categories()
        config_module.find_current_profile()
        ###-- END OF BACK-END PART --###



        ###-- FRON-END PART --###
        front_end_app = FrontApp()
        front_end_app.set_conf_module(config_module)
        front_end_app.run()
        ###-- END OF FRON-END PART --###

###-- !!!END OF MAIN ZONE!!! --###

if __name__ == "__main__":
    app = MainApp()
    app.start()





