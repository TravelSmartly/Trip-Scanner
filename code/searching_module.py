class Searching_module(App):
    m_object_list = None
    search_counter = 0

    def get_m_object_list(self):
        return self.m_object_list
    def set_m_object_list(self,list):
        self.m_object_list = list
    def search_the_area(self):
        pass
    # def check_proximity(self):
    #     pass
    def remove_old_objects(self):
        pass
    def start_searching_module(current_location):
        if (current_location == ()):
            return -2
        elif (-90 < current_location[0] < 90 or  -180 < current_location[1] < 180):
            return -1
        else:
            return 0
