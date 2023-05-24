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


    def __init__(self, conf_module: object):
        ### INITIALIZATION ###
        super().__init__(conf_module)


    def hi(self):
        print("hi profile adapter")


    def postprocessing(self):
        ## PROFILE DOWNLOADING
        self.download_profiles()
        profiles = self.get_profiles_raw()

        if len(profiles) == 0:
            return -1
        self.profile_refreshed = 1

        self.profiles = profiles
        selected = self.download_selected_profile()
        self.selected = selected

        return 0


    ## DG: added download_selected_profile, which allows to download right away selected_profile from back_end
    def download_selected_profile(self):
        selected = self.conf_module.put_selected_profile_to_front()
        return selected


    def get_instraction(self):
        return self.instraction

    ## DG: added get_selected_profile
    def get_selected(self):
        return self.selected

    def get_profiles(self):
        ## ! Zwracam wskaznik do profilow, wiec zmiana
        ## bedzie dokonana wszedzie
        return self.profiles

    def set_profiles_instraction(self, pro_inst):
        self.instraction = pro_inst


## DG: ! Dodalem Profile_manipulator, aby zdjac ladunek manipulowania interfejsem profilu, by trzymac sie zasad SOLID, ale mozna bylo tego nie robic
## (EN)I added Profile_manipulator to take the load off from Profile_adapter

class Profile_manipulator(Profile_adapter):
    is_categories_changed = 0
    last_changed_categories_id = -1
    first_changed_categories_id = -1
    def __init__(self, conf_module: object):
        ### INITIALIZATION ###
        super().__init__(conf_module)

    ## ! Zmienam wybrane kategorie bezposrednio w calym Profile_manipulator
    ## uwazam, ze nie ma potrzeby robic oddzielna liste ze zmianami
    ## poniewaz utrudni to kontrole, z tego wzgledu, iz trzeba
    ## bedzie caly czas dbac o to, aby w tej liscie byly aktualne dane
    ## a teraz w calej mojej systemie beda aktualne dane, ale
    ## trzeba pamietac o tym, ze zmiana bedzie wszedzie

    ## Tutaj jest zaleznosc miedzy aktualnym profilem,
    ## wiec jesli gdzies go zmienie, to zmieni sie on wszedzie,
    ## ale w moim przypadku dbam o dobra hermetycznosc
    def select_category(self, id: int) -> int:
        if id is None and type(id) is not int:
            return -1
        sel_cat = self.get_selected_categories()
        if sel_cat == -1:
            return -1

        if id not in sel_cat:
            sel_cat.append(id)

        # print(self.get_selected()[self.get_instraction()["categories"]], "ON")
        ## If first element has been changed double time, then i don't change nothing
        to_rechenge = 0
        if self.first_changed_categories_id == id:
            self.is_categories_changed = 0
            to_rechenge = 1
        self.first_changed_categories_id = -1

        if not self.is_categories_changed and to_rechenge == 0:
            ## w przypadku, gdy uzytkownik odznaczyl i jeszcze raz zaznaczyl
            ## ta sama kategoroie, to nic nie zmieniam
            self.first_changed_categories_id = id
            self.is_categories_changed = 1

        # print(self.last_changed_categories_id, " LAST ", self.first_changed_categories_id, " FIRST", self.is_categories_changed, " CHAGES? ")

        return 0

    def deselect_category(self, id: int) -> int:
        if id is None and type(id) is int:
            return -1

        sel_cat = self.get_selected_categories()
        if sel_cat == -1:
            return -1

        if id in sel_cat:
            sel_cat.remove(id)

        # print(self.get_selected()[self.get_instraction()["categories"]], "OFF")
        ## If first element has been changed double time
        to_rechenge = 0
        if self.first_changed_categories_id == id:
            self.is_categories_changed = 0
            to_rechenge = 1
        self.first_changed_categories_id = -1

        if not self.is_categories_changed and to_rechenge == 0:
            self.first_changed_categories_id = id
            self.is_categories_changed = 1


        # print(self.last_changed_categories_id, " LAST ", self.first_changed_categories_id, " FIRST", self.is_categories_changed, " CHAGES? ")

        return 0


    def prepare_send_profile(self) -> int:
        # selected_profile = self.get_selected()
        profiles = self.get_profiles()
        if profiles is None and type(profiles) is not dict:
            return -1
        # print(profiles)
        did_send_correctly = self.send_profile(profiles)
        if did_send_correctly == 0:
            return 0
        else:
            return did_send_correctly

    ## Init changes odpowiada za inicjalizacja wybranych categorii
    def get_selected_categories(self):
        selected_profile = self.get_selected()
        if selected_profile is None and type(selected_profile) is not dict:
            return -1
        return selected_profile[self.get_instraction()["categories"]]

    ## Zwraca, czy zostalo cos zmodyfikowane w kategoriach
    def get_change_status(self):
        return self.is_categories_changed

## DG: ! I have splited the Profile_adapter into Profile_adapter and Category_adapter, which may help to better understand the code
class Category_adapter(Profile_provider):
    ## DG: dodałem selected_categories, for storing new postprocesing categories
    selected_categories = []
    ## DG: processed categories
    categories = []
    ## DG: contains how to read category array, because I will get categories from back_end I need dictionary
    ## to be sure about the data I will put in the list
    instraction = {
        "id": "id",
        "name": "category",
        "icon": "icon"
    }

    def __init__(self, conf_module: object):
        ### INITIALIZATION ###
        super().__init__(conf_module)

    def hi(self):
        print("hi categories adapter")

    ## DG: Added categories_postprocessing
    def postprocessing(self) -> int:
        # profiles = self.get_profiles()
        # if len(profiles) != 0:
        #     return -1
        # self.profile_refreshed = 0
        ## CATEGORIES DOWNLOADING
        self.download_categories()
        categories = self.get_categories_raw()
        self.categories = categories["Categories"]
        return 0

    def get_categories(self) -> list:
        return self.categories

    def get_instraction(self) -> dict:
        return self.instraction

    def set_instraction(self, cat_inst: dict):
        self.instraction = cat_inst

    def set_categories(self):
        pass
