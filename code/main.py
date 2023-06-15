### libraries
import os
import json
import pathlib
from time import time
from kivy.app import App
from kivy.utils import platform
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
# from .front_end.content.Map_section.gpshelper import GpsHelper
###---- END OF IMPORT FRONT-END AND PACKAGES ----###

# Window.size = (360, 640)

###-- END OF FRONT-END ZONE --###



###-- !!!START MAIN ZONE!!! --###

## DG: ! We changed name "main" to "MainApp"!
class MainApp:

    def start(self):
        ###-- BACK-END PART --###
        ### GPS system -> may not work on devices other than android!
        ### starts updating current phone location
        ### To get current phone user location, use: 
        ### Location_module.get_current_location()
        ### There is no need to create an object of this type
        ### Just operate on class itself
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            from plyer import gps
            from plyer import notification
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET, Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])
            gps.configure(on_location=Location_module.on_gps_location)
            gps.start(minTime=1000, minDistance=0)

        ###########################################################
        config_module = Configuration_module()
        config_module.create_config_file()
        profile_import_status = config_module.read_profiles()
        categories_import_status = config_module.read_categories()
        categories_line_import_status = config_module.read_categories_txt()
        # print(categories_import_status, profile_import_status)
        config_module.find_current_profile()

        arranging_module = Arranging_module()

        searcher = Searching_module()
        searcher.set_config_module(config_module)
        ###-- END OF BACK-END PART --###



        ###-- FRON-END PART --###
        ###-- FRON-END INIT PART --###
        front_end_app = FrontApp()
        ###-- END OF FRON-END INIT PART --###
        front_end_app.set_conf_module(config_module)
        front_end_app.set_location_module(Location_module)
        front_end_app.set_arranging_module(arranging_module)
        front_end_app.set_search_module(searcher)
        front_end_app.run()
        ###-- END OF FRON-END PART --###

###-- !!!END OF MAIN ZONE!!! --###

if __name__ == "__main__":
    app = MainApp()
    app.start()





