import json

## Zadaniem Profile_provider tylko sciągnąć dane z back_endu


class Profile_provider:
    ## DG: usunełem sub_categories, zamiast tego, zrobiłem categories_raw, ktore ma takze inna nazwe, wczesniej bylo categories dict in list
    categories_raw = []
    # categories = []
    # profiles = []
    ## DG: zaminilem nazwe z profiles na profiles_raw, podkreslajac, ze te profile sa surowe i potrzebuj dodatkowej obrobki
    profiles_raw = []
    ## DG: nowa zmienna profile_refreshed, sluzy do tego, aby sie dowiedziec, czy profil sie odswierzyl
    profile_refreshed = 0
    # categories_url = "categories/generalized_categories.json"
    # profile_url = "categories/profiles.json"
    conf_module = None



    def __init__(self, conf_module: object):
        ### INITIALIZATION conf_module###
        # if isinstance(conf_module, object):
        self.conf_module = conf_module

        ## OOn the start I want to have categories
        self.download_categories()

    ## CATEGORIES DOWNLOADING FROM BACK END
    def download_categories(self) -> int:
        # if self.conf_module is None:
        #     return -1
        # if hasattr(self.conf_module, 'put_profile_front') == 0:
        #     return -1
        # self.profiles = self.conf_module.put_profile_front()
        # self.profile_refreshed = 1
        # profiles = self.profiles
        self.categories_raw = self.conf_module.put_categories_to_front()

        # print(self.categories)

        return 0

    ## DG: Added download_profiles, because I have to download profile separately
    def download_profiles(self) -> int:
        # try:
        #     f = open(self.profile_url)
        #     profiles = json.load(f)
        #     self.profiles_raw = profiles
        # except Exception as e:
        #     self.profiles_raw = []
        self.profiles_raw = self.conf_module.put_profiles_to_front()

        self.profile_refreshed = 1

        return 0

    ## DG: send_categories changed on send_profile, becuse instead sending categories, which is const,
    ## we sending profile with selected categories
    ## I assume, that profile is selected profile, but could be anything else
    def send_profile(self, profiles = None) -> int:
        # print(self.conf_module, " SEND")
        did_send_correctly = self.conf_module.save_profiles()
        if did_send_correctly != 0:
            return -1
        # self.conf_module.hi()
        # if hasattr(self.conf_module, 'save_profiles') == 0:
        #     return -1
        # self.conf_module.save_profiles(profile)
        self.profile_refreshed = 0
        return 0


    ## DG: get_categories changed name to get_categories_raw and the same with profiles
    def get_categories_raw(self):
        return self.categories_raw
    def get_sub_categories(self): pass
    def get_profiles_raw(self) -> list:
        return self.profiles_raw

    def set_sub_categories(self): pass
    def set_profiles(self): pass