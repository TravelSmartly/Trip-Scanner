import json

## Zadaniem Profile_provider tylko sciągnąć dane z back_endu


class Profile_provider:
    ## DG: usunełem sub_categories, zamist tego, zrobiłem categories dict in list
    categories = []
    profiles = []
    ## DG: nowa zmienna profile_refreshed, sluzy do tego, aby sie dowiedziec, czy profil sie odswierzyl
    profile_refreshed = 0
    categories_url = "categories/generalized_categories.json"
    profile_url = "categories/profiles.json"
    conf_module = None
    def __init__(self, conf_module):
        ### INITIALIZATION conf_module###
        if isinstance(conf_module, object):
            self.conf_module = conf_module

        ## OOn the start I want to have categories
        self.download_categories()

    ## CATEGORIES DOWNLOADING FROM BACK END
    def download_categories(self):
        # if self.conf_module is None:
        #     return -1
        # if hasattr(self.conf_module, 'put_profile_front') == 0:
        #     return -1
        # self.profiles = self.conf_module.put_profile_front()
        # self.profile_refreshed = 1
        # profiles = self.profiles
        try:
            f = open(self.categories_url)
            self.categories_raw = json.load(f)
        except Exception as e:
            self.categories_raw = []

        # print(self.categories)

        return 0

    ## DG: Added download_profiles, because I have to download profile separately
    def download_profiles(self):
        try:
            f = open(self.profile_url)
            profiles = json.load(f)
            self.profiles_raw = profiles
        except Exception as e:
            self.profiles_raw = []

        profile_refreshed = 1

        return 0

    ## DG: send_categories changed on send_profile, becuse instead sending categories, which is const,
    ## we sending profile with selected categories
    def send_profile(self, profile):
        if hasattr(self.conf_module, 'put_to_profile_front') == 0:
            return -1
        self.conf_module.put_to_profile_front(profile)
        profile_refreshed = 0
        return 0


    ## DG: get_categories changed name to get_categories_raw and the same with profiles
    def get_categories_raw(self):
        return self.categories_raw
    def get_sub_categories(self): pass
    def get_profiles_raw(self):
        return self.profiles_raw

    def set_sub_categories(self): pass
    def set_profiles(self): pass