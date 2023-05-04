class Searching_module():
    m_object_list = None #first element is current_location
    search_counter = 0
    # init method or constructor
    def __init__(self, current_location):
        self.m_object_list = []
        self.m_object_list[0]=current_location



    def get_m_object_list(self):
        return self.m_object_list
    def set_m_object_list(self,list):
        self.m_object_list = list
    def search_the_area(self):
        pass
    def remove_old_objects(self):
        pass
    def start_searching_module(current_location):
        if (current_location == ()):
            return -2
        elif (-90 < current_location[0] < 90 or -180 < current_location[1] < 180):
            return -1
        else:
            return 0
