
from arranging_module import Arranging_module
import pytest

@pytest.fixture
def arranging_module():
    return Arranging_module()

def test_categorize_obj():
    arranging_module = Arranging_module()
    map_object = {} #Set fixed existing objects
    arranging_module.categorize_obj(map_object)
    # Replace the assert statement with your expected outcome
    assert arranging_module.categorize_obj(map_object) == None

def test_sort_obj():
    arranging_module = Arranging_module()
    map_object = {} #Set fixed existing objects
    arranging_module.sort_obj(map_object)
    # Replace the assert statement with your expected outcome
    assert arranging_module.sort_obj(map_object) == None

def test_start_arranging_module():
    arranging_module = Arranging_module()
    kwargs = {}
    arranging_module.start_arranging_module(**kwargs)
    # 0 If its correct
    assert arranging_module.start_arranging_module(**kwargs) == 0

def test_provide_object():
    arranging_module = Arranging_module()
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_list = [4, 5, 6]
    arranging_module.provide_object(my_dict, my_list)
    # Replace the assert statement with your expected outcome
    assert arranging_module.provide_object(my_dict, my_list) == None