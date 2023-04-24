from searching_module import Searching_module
import pytest

@pytest.fixture
def searching_module():
    return Searching_module()

    def search_the_area(searching_module):
        r=100
        listobject = searching_module.search_the_area(r,(50.060683036581125, 19.935779508513296))
        assert listobject.isNotEmpty()

        listobject = searching_module.search_the_area(r,(-56.61335002485333, -11.054544822997077))
        assert listobject.isEmpty()

    def test_remove_old_objects(searching_module):
        #add object
        map_object0 = {"id": 334234, "name": "a Grande Mamma", "category": None,
                       "coordinates": (50.06163905474776, 19.936530642326513), "description": None,
                       "rating": None}  # Set fixed existing objects
        map_object1 = {"id": 43243, "name": "Aparthotel Stare Miasto", "category": None,
                       "coordinates": (50.06182501735149, 19.933510474939244), "description": None, "rating": (4.2, 60)}
        searching_module.m_object_list = [map_object0, map_object1]

        map_object2 = {"id": 324243, "name": "test", "category": None,
                       "coordinates": (51.06182501735149, 65.933510474939244), "description": None, "rating": (4.0, 20)}
        new_list = [map_object2]




        #check if object exist
        assert searching_module.m_object_list is not None
        #remove object
        searching_module.remove_old_objects(new_list)
        #check if list of object decreased/zeroed
        assert searching_module.m_object_list == new_list
        #nadpisuje stare miejsce


    #def test_start_searching_module(searching_modulet):
        #assert searching_module.start_searching_module((51.06182501735149, 65.933510474939244)) == 0


