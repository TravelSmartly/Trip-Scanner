from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
from android.hardware import hardware_android

class Localisation_module(App):
    def get_gps_location(on_location_update):
        request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION])
        location_provider = hardware_android.get_location_provider()
        location_provider.configure(on_location=self.on_location_update)
        location_provider.start()
        return Label(text="Getting GPS location...")

    def on_stop(self):
        location_provider.stop()

    #to moze byc w pliku konfiguracyjnym:
    def on_location_update(**kwargs):
        latitude = kwargs['lat']
        longitude = kwargs['lon']
        print("Latitude:", latitude)
        print("Longitude:", longitude)


