from localisation_module import Localisation_module
import pytest


@pytest.fixture
def localisation_module():
    return Localisation_module()


def test_get_current_location(localisation_module):
    # check if location return is not empty thing
    assert localisation_module.get_current_location() is not None


def test_check_proximity(localisation_module):
    r=100
    current_location = (50.06163905474776, 19.936530642326513)
    real_pos = (50.06182501735149, 19.933510474939244)
    assert localisation_module.Check_proximity(r,current_location,real_pos) = True #Check proximiy ((current_location[0]-real_pos[0])**2 + (current_location[1]-real_pos[1])**2) < r

    real_pos = (50.05301179901293, 19.914758618374478)
    assert localisation_module.Check_proximity(r, current_location, real_pos) = False
    #r, current_location, faktycznalokalizacji

    # set fixed location check whats nearbly



def test_on_start(localisation_module):
    #
    assert localisation_module.on_start() == None


def test_put_user_location_front(localisation_module):
    #
    assert localisation_module.put_user_location_front() == None


def test_start_location_module(monkeypatch, localisation_module):
    #
    mock_start_location_module = MagicMock()

    #
    monkeypatch.setattr(localisation_module, 'start_location_module', mock_start_location_module)

    #
    localisation_module.start_location_module()
    mock_start_location_module.assert_called_once()

# def on_gps_location(self,**kwargs):
#     print(kwargs['lat'],kwargs['lon'])
#     #save these values to file