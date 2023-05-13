import json

## Zadaniem Profile_provider tylko sciągnąć dane z back_endu


class Profile_provider:
    ## DG: usunełem sub_categories, zamist tego, zrobiłem categories dict
    ##! Usuń komentarz, po uzgodnieniu kanwencji kategorii
    # categories = (
    #     {
    #         "id": 0,
    #         "Category": "Option0"
    #         ""
    #     },
    #     {
    #         "id": 1,
    #         "Category": "Option1"
    #     },
    #     {
    #         "id": 2,
    #         "Category": "Option2"
    #     },
    #     {
    #         "id": 3,
    #         "text": "Option3"
    #     },
    #     {
    #         "id": 4,
    #         "text": "Option4"
    #     },
    #     {
    #         "id": 5,
    #         "text": "Option5"
    #     }
    # )
    categories = []
    changes = []
    profiles = []
    ## DG: nowa zmienna profile_refreshed, sluzy do tego, aby sie dowiedziec, czy profil sie odswierzyl
    profile_refreshed = 0
    categories_url = "categories/generalized_categories.json"
    profile_url = "categories/profiles.json"
    def __init__(self, conf_module):
        ### INITIALIZATION conf_module###
        self.conf_module = None
        if isinstance(conf_module, object):
            self.conf_module = conf_module

        ## CATEGORIES DOWNLOADING
        self.download_categories()



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

        return 0


    ## DG: get_categories changed name to get_categories_raw and the same with profiles
    def get_categories_raw(self):
        return self.categories_raw
    def get_sub_categories(self): pass
    def get_profiles_raw(self):
        return self.profiles_raw

    def set_sub_categories(self): pass
    def set_profiles(self): pass