from location_module import Location_module
import pytest
import time


@pytest.fixture
def location_module():
    return Location_module()


def test_get_current_location(location_module):
    # checking coordinates when user on Rynek Glowny: 50.0615388,19.9398953
    assert 50.06153 < location_module.get_current_location()[0] < 50.06154 and 19.93989 < location_module.get_current_location()[1] < 19.939896


def test_check_proximity(location_module):
    r=100
    current_location = (50.06163905474776, 19.936530642326513)
    real_pos = (50.06182501735149, 19.933510474939244)
    assert location_module.Check_proximity(r,current_location,real_pos) == True #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r

    real_pos = (50.05301179901293, 19.914758618374478)
    assert location_module.Check_proximity(r, current_location, real_pos) == False
    #r, current_location, faktycznalokalizacji

    # set fixed location check whats nearbly
    

def test_start_location_module(monkeypatch, localisation_module):
    seconds = 3
    for i in range (10):
        time.sleep(seconds)
        assert location_module.start_location_module() == 0

# def on_gps_location(self,**kwargs):
#     print(kwargs['lat'],kwargs['lon'])
#     #save these values to file
