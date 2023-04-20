from localisation_module import Localisation_module
import pytest


@pytest.fixture
def localisation_module():
    return Localisation_module()


def test_get_current_location(localisation_module):
    # check if location return is not empty thing
    assert localisation_module.get_current_location() is not None


def test_check_proximity(localisation_module):
    r, current_location, faktycznalokalizacji

    # set fixed location check whats nearbly

    assert localisation_module.chech_proximity() == None


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