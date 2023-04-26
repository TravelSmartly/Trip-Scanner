
from arranging_module import Arranging_module
import searching_module
import pytest

@pytest.fixture
def arranging_module():
    return Arranging_module()

def test_categorize_obj(arranging_module):
    #arranging_module = Arranging_module()
    map_object0 = {"id": 334234, "name": "a Grande Mamma", "category": None, "coordinates":(50.06163905474776, 19.936530642326513), "description": None, "rating": None } #Set fixed existing objects
    map_object1 = {"id": 43243, "name": "Aparthotel Stare Miasto", "category": None, "coordinates": (50.06182501735149, 19.933510474939244), "description": None, "rating": (4.2,60)}
    #arranging_module.categorize_obj(map_object)

    object_list=[map_object0, map_object1]
    listofcategories = arranging_module.categorize_obj(object_list)
    map_object0["category"] = listofcategories[0]
    map_object1["category"] = listofcategories[1]
    assert map_object0["category"] == ("restaurant","bar")
    assert map_object0["category"] == ("hotel")
    #przypisuje category-> tuple

#if booking.com - hotel(somethinglike that)
def test_sort_obj(arranging_module):

    map_object0 = {"id": 334234, "name": "a Grande Mamma", "category": "restaurant", "coordinates":(30.06163905474776, 48.936530642326513), "description": None, "rating": None } #Set fixed existing objects
    map_object1 = {"id": 43243, "name": "Aparthotel Stare Miasto", "category": None, "coordinates": (50.06182501735149, 49.933510474939244), "description": None, "rating": (4.2,60)}
    map_object2 = {"id": 43443, "name": "test", "category": "hotel", "coordinates": (87.06182501735149, 82.933510474939244), "description": None, "rating": (1.2, 40)}
    # a = searching_module.Searching_module()
    # a.set_m_object_list([map_object0, map_object1, map_object2])
    object_list = [(50,50),map_object0, map_object1, map_object2]
    object_list = arranging_module.sort_obj("rating",object_list)
    assert object_list[1] == map_object1
    assert object_list[2] == map_object2
    assert object_list[3] == map_object0

    object_list = arranging_module.sort_obj("distance",object_list)
    assert object_list[1] == map_object1
    assert object_list[2] == map_object0
    assert object_list[3] == map_object2

    object_list = arranging_module.sort_obj("category",object_list)
    assert object_list == -1

    map_object1 = {"id": 43243, "name": "Aparthotel Stare Miasto", "category": "moto",
                   "coordinates": (50.06182501735149, 49.933510474939244), "description": None, "rating": (4.2, 60)}
    object_list = [(50, 50), map_object0, map_object1, map_object2]
    object_list = arranging_module.sort_obj("category", object_list)
    assert object_list[1] == map_object2
    assert object_list[2] == map_object1
    assert object_list[3] == map_object0




def test_start_arranging_module():
    a = searching_module.Searching_module()
    b = None
    assert arranging_module.start_arranging_module(a) == 0
    assert arranging_module.start_arranging_module(b) == -2

def test_provide_objects():
    a = searching_module.Searching_module()
    map_object0 = {"id": 334234, "name": "a Grande Mamma", "category": None, "coordinates":(50.06163905474776, 19.936530642326513), "description": None, "rating": None } #Set fixed existing objects
    map_object1 = {"id": 43243, "name": "Aparthotel Stare Miasto", "category": None, "coordinates": (50.06182501735149, 19.933510474939244), "description": None, "rating": (4.2,60)}
    a.set_m_object_list([map_object0, map_object1])

    assert arranging_module.provide_objects() == a.get_m_object_list()

