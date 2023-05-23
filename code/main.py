### libraries
import os
from time import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from plyer import gps
from plyer import notification


### classes
#from classes import Configuration

###-- FRONT-END ZONE --###
""" 
Od tego miejsca zaczyna się działać front-end, w tej chwili od razu odpala się cały interfejs, 
ale później powinno się zaczynać od maina w tym miejscu. 
"""

Window.size = (360, 640)
### IMPORT FRONT-END AND PACKAGES ###
"""
Importuję w tym przypadku front_end/__init__.py
"""
from front_end.__init__ import *

###-- END OF FRONT-END ZONE --###

front_end_app = FrontApp()
front_end_app.run()







