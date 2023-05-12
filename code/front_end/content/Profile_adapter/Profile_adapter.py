from .Profile_provider import Profile_provider
import time

class Profile_adapter(Profile_provider):

    def __init__(self, conf_module):
        # DG: dodałem selected_categories, dla przetworzenia nowych kategorii
        self.selected_categories = {}

        ### INITIALIZATION ###
        super().__init__(conf_module)

    def profile_postprocessing(self):
        profiles = self.get_profiles()
        if len(profiles) != 0:
            return -1

        self.profile_refreshed = 0
        return 0
    def send_categories(self, cat):
        if hasattr(self.conf_module, 'put_to_profile_front') == 0:
            return -1
        self.conf_module.put_to_profile_front(self.changes)
        self.changes.clear()
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

