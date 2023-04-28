import time
#from content.Providers.User_location_provider import User_location_provider
#from content.Providers.User_location_provider import User_location_provider

class User_location_provider:
    def hi(self): print("HI")
    def __init__(self, location_module):
        # VAR SETTING
        # DG: location swap on curr_location
        self.curr_location = ()

        ### INITIALIZATION ###
        self.loc_module = None
        if isinstance(location_module, object):
            self.loc_module = location_module


    def download_location(self):
        if self.loc_module is None:
            return -1
        if hasattr(self.loc_module, 'get_current_location') == 0:
            return -1
        # czy pobrane dane są poprawne
        self.curr_location = self.loc_module.get_current_location()
        return 0

    def success(self): pass
    def error(self): pass
    def failure(self): pass

    def get_curr_location(self):
        if self.curr_location is None:
            return -1
        return self.curr_location

    def set_curr_location(self): pass

########### ADAPTER #######

class User_location_adapter(User_location_provider):
    def __init__(self, location_module):
        # historia lokacji
        # DG: type swaped from dict to list
        self.location_data = []
        # DG: dodałem nową zmienną time, która oznacza czas pobrania w unix
        self.u_time = 1682657624
        # DG: dodałem my_loc, to jest zmienna, która przechowuje również datę pobrania
        self.my_loc = {}

        ### INITIALIZATION ###
        super().__init__(location_module)

    def location_postprocessing(self):
        is_dl = self.download_location()
        if is_dl == -1:
            return -1
        loc = self.get_curr_location()

        u_time = int(time.time())
        self.my_loc["loc"] = loc
        self.my_loc["downlload_loc"] = u_time
        self.location_data.append(self.my_loc)

    def get_location_data(self):
        if self.location_data is None:
            return -1
        return self.location_data

    def set_location_data(self): pass
