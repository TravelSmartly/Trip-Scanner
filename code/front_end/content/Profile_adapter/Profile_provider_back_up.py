class Profile_provider:
    def __init__(self, conf_module):
        # DG: usunełem sub_categories, zamist tego, zrobiłem categories dict
        self.categories = [
            {
                "name": "hi",
                "queue": 1,
                "subcats": ("hi_mini", "hi_bigi"),
                "selected": 0
            },
            {
                "name": "hello",
                "queue": 2,
                "subcats": ("hello_mini", "hello_bigi"),
                "selected": 1
            }
        ]
        self.changes = []
        self.profiles = ()
        # DG: nowa zmienna profile_refreshed
        self.profile_refreshed = 0

        ### INITIALIZATION ###
        self.conf_module = None
        if isinstance(conf_module, object):
            self.conf_module = conf_module
    def download_categories(self):
        if self.conf_module is None:
            return -1
        if hasattr(self.conf_module, 'put_profile_front') == 0:
            return -1
        self.profiles = self.conf_module.put_profile_front()
        self.profile_refreshed = 1
        profiles = self.profiles
        return 0



    def get_categories(self): pass
    def get_sub_categories(self): pass
    def get_profiles(self):
        return self.profiles

    def set_categories(self): pass
    def set_sub_categories(self): pass
    def set_profiles(self): pass