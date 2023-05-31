from kivymd.app import MDApp
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from functools import partial

class GpsHelper():
    has_centered_map = False
    def run(self):
        my_map = MDApp.get_running_app().root.ids.nav_bar_id.ids.map_section_id.ids.mapview
        self.map = my_map
        # gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        self.gps_blinker = my_map.ids.blinker
        # print(self.gps_blinker)
        self.gps_blinker.blink()
        ## Odswierzam lokalizacje
        # self.update_blinker_position(lat=30, lon=30)
        Clock.schedule_interval(self.update_blinker_position, 5)


        # Request permissions on Android
        # if platform == 'android':
        #     from android.permissions import Permission, request_permissions
            # def callback(permission, results):
            #     if all([res for res in results]):
            #         print("Got all permissions")
            #         from plyer import gps
            #         gps.configure(on_location=self.update_blinker_position,
            #                       on_status=self.on_auth_status)
            #         gps.start(minTime=1000, minDistance=0)
            #     else:
            #         print("Did not get all permissions")
            #
            # request_permissions([Permission.ACCESS_COARSE_LOCATION,
            #                      Permission.ACCESS_FINE_LOCATION], callback)



    def update_blinker_position(self, dt):
        # print(args)
        location_module = MDApp.get_running_app().loc_module
        loction = location_module.get_current_location()
        # print(loction)
        # my_lat = kwargs['lat']
        # my_lon = kwargs['lon']
        my_lat = loction[0]
        my_lon = loction[1]
        # print("GPS POSITION", my_lat, my_lon)
        # Update GpsBlinker position
        # gps_blinker = MDApp.get_running_app().root.ids.mapview.ids.blinker
        # self.gps_blinker = gps_blinker
        self.gps_blinker.lat = my_lat
        self.gps_blinker.lon = my_lon
        self.map.trigger_update(0)

        # Center map on gps
        if not self.has_centered_map:

            self.map.center_on(my_lat, my_lon)
            self.has_centered_map = True


    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
        # dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()


# class GpsHelper():
#     has_centered_map = False
#
#     def run(self):
#         # Get a reference to GpsBlinker, then call blink()
#         gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
#         # Start blinking the GpsBlinker
#         gps_blinker.blink()
#
#         # Request permissions on Android
#         if platform == 'android':
#             from android.permissions import Permission, request_permissions
#             def callback(permission, results):
#                 if all([res for res in results]):
#                     print("Got all permissions")
#                     from plyer import gps
#                     gps.configure(on_location=self.update_blinker_position,
#                                   on_status=self.on_auth_status)
#                     gps.start(minTime=1000, minDistance=0)
#                 else:
#                     print("Did not get all permissions")
#
#             request_permissions([Permission.ACCESS_COARSE_LOCATION,
#                                  Permission.ACCESS_FINE_LOCATION], callback)
#
#         # Configure GPS
#         if platform == 'ios':
#             from plyer import gps
#             gps.configure(on_location=self.update_blinker_position,
#                           on_status=self.on_auth_status)
#             gps.start(minTime=1000, minDistance=0)
#
#
#     def update_blinker_position(self, *args, **kwargs):
#         my_lat = kwargs['lat']
#         my_lon = kwargs['lon']
#         print("GPS POSITION", my_lat, my_lon)
#         # Update GpsBlinker position
#         gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
#         gps_blinker.lat = my_lat
#         gps_blinker.lon = my_lon
#
#         # Center map on gps
#         if not self.has_centered_map:
#             map = App.get_running_app().root.ids.mapview
#             map.center_on(my_lat, my_lon)
#             self.has_centered_map = True
#
#
#     def on_auth_status(self, general_status, status_message):
#         if general_status == 'provider-enabled':
#             pass
#         else:
#             self.open_gps_access_popup()
#
#     def open_gps_access_popup(self):
#         dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
#         dialog.size_hint = [.8, .8]
#         dialog.pos_hint = {'center_x': .5, 'center_y': .5}
#         dialog.open()