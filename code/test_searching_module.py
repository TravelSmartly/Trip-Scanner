from searching_module import Searching_module
import pytest

@pytest.fixture
def searching_module():
    return Searching_module()

    def search_the_area(self):
        r=100
        listobject = localisation_module(r,(50.060683036581125, 19.935779508513296))
        assert listobject.isNotEmpty()

        listobject = localisation_module(r,(-56.61335002485333, -11.054544822997077))
        assert listobject.isEmpty()

    def test_remove_old_objects(self):
        pass
    def test_start_searching_module(self,*args):
        pass
