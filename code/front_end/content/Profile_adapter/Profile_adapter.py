from .Profile_provider import Profile_provider
import time
## Zadaniem Profile_adapter jest przetworzyc dane, ktory sciagnal Profile_provider,
## poniewaz dane, ktore ma profile_provider sa ogolne, a tu nalezy je uszczegolowic


class Profile_adapter(Profile_provider):
    ## DG: profile_refreshed means, that I download profile from phone again
    profile_refreshed = 0
    ## DG: processed profiles
    profiles = []
    ## DG: contains how to read profile array, because I will get profiles from back_end I need dictionary
    ## to be sure about the data I will put in the list
    instraction = {
        "id": "id",
        "name": "name",
        "selected": "selected",
        "categories": "categories",
        "icon": "icon"
    }
    selected = None


    def __init__(self, conf_module):
        ### INITIALIZATION ###
        super().__init__(conf_module)


    def hi(self):
        print("hi profile adapter")


    def postprocessing(self):
        ## PROFILE DOWNLOADING
        self.download_profiles()
        profiles = self.get_profiles_raw()["profiles"]

        if len(profiles) == 0:
            return -1
        self.profile_refreshed = 1

        self.profiles = profiles
        selected = self.download_selected_profile()
        self.selected = selected

        return 0


    ## DG: send_categories changed on send_profile, becuse instead sending categories, which is const,
    ## we sending profile with selected categories
    def send_profile(self, cat):
        if hasattr(self.conf_module, 'put_to_profile_front') == 0:
            return -1
        self.conf_module.put_to_profile_front(self.changes)
        self.changes.clear()
        return 0

    ## DG: added download_selected_profile, which allows to download right away selected_profile from back_end
    def download_selected_profile(self):
        profiles = self.get_profiles()
        for profile in profiles:
            if profile["selected"] == 1:
                return profile

        return -1


    def get_instraction(self):
        return self.instraction
    ## DG: added get_selected_profile
    def get_selected(self):
        return self.selected
    def get_profiles(self):
        return self.profiles

    def set_profiles_instraction(self, pro_inst):
        self.instraction = pro_inst



##! DF: I have split the Profile_adapter into Profile_adapter and Category_adapter, which may help to better understand the code

class Category_adapter(Profile_provider):
    ## DG: dodałem selected_categories, for storing new postprocesing categories
    selected_categories = {}
    ## DG: processed categories
    categories = []
    ## DG: contains how to read category array, because I will get categories from back_end I need dictionary
    ## to be sure about the data I will put in the list
    instraction = {
        "id": "id",
        "name": "category",
        "icon": "icon"
    }


    def __init__(self, conf_module):
        ### INITIALIZATION ###
        super().__init__(conf_module)


    def hi(self):
        print("hi categories adapter")


    ## DG: Added categories_postprocessing
    def postprocessing(self):
        # profiles = self.get_profiles()
        # if len(profiles) != 0:
        #     return -1
        # self.profile_refreshed = 0
        ## CATEGORIES DOWNLOADING
        self.download_categories()
        categories = self.get_categories_raw()
        self.categories = categories["Categories"]
        return 0


    def select_cat(self, id):
        if id is None:
            return -1
        if type(id) is int:
            return -1

        self.changes.append(id)
        self.categories[id]["selected"] = 1
        return 0


    def deselect_cat(self, id):
        if id is None:
            return -1
        if type(id) is int:
            return -1
        self.changes.append(id)
        self.categories[id]["selected"] = 0
        return 0

    def get_categories(self):
        return self.categories
    def get_instraction(self):
        return self.instraction

    def set_instraction(self, cat_inst):
        self.instraction = cat_inst
    def set_categories(self):
        pass

