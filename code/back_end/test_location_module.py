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

    
    r=50
    current_location = (69.3682237466593, -24.42319080312447)
    real_pos = (69.36821391928645, -24.422031815099345)
    assert location_module.Check_proximity(r,current_location,real_pos) == True #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r

    current_location = (69.36822702244923, -24.42319080312447)
    real_pos = (69.36819754032172, -24.42174981533922)
    assert location_module.Check_proximity(r,current_location,real_pos) == False #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r


    current_location = (4.977345975972701, 21.576657045476846)
    real_pos = (4.977367633967908, 21.57706401783827)
    assert location_module.Check_proximity(r,current_location,real_pos) == True #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r


    current_location = (4.977346842292529, 21.576657045476846)
    real_pos = (4.9773693666075, 21.577157934537063)
    assert location_module.Check_proximity(r,current_location,real_pos) == False #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r


    r=200

    current_location = (79.84918915447686, 13.305728818397744)
    real_pos = (79.84916896262257, 13.31498036866999)
    assert location_module.Check_proximity(r,current_location,real_pos) == True #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r


    current_location = (79.84918158253616, 13.305728818397744)
    real_pos = (79.84913867476658, 13.3169710273199)
    assert location_module.Check_proximity(r,current_location,real_pos) == False #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r


    current_location = (4.977347792469449, 21.57665580343438)
    real_pos = (4.977334178714007, 21.578289781305845)
    assert location_module.Check_proximity(r,current_location,real_pos) == True #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r

    current_location = (4.9773439028250746, 21.576659707802055)
    real_pos = (4.977310840846875, 21.578648983131835)
    assert location_module.Check_proximity(r,current_location,real_pos) == False #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r
    



    # set fixed location check whats nearbly
    

def test_start_location_module(monkeypatch, localisation_module):
    seconds = 3
    for i in range (10):
        time.sleep(seconds)
        assert location_module.start_location_module() == 0

# def on_gps_location(self,**kwargs):
#     print(kwargs['lat'],kwargs['lon'])
#     #save these values to file
