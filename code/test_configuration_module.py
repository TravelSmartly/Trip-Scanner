from configuration_module import Configuration_module
import pytest


@pytest.fixture
def configuration_module():
    return Configuration_module()


def test_start_configuration_module(configuration_module):
    pass

def test_save_profile(configuration_module,current_profile):
    #open profile
    #modify something
    #save profile
    #close
    #open again
    #assert modified thing is still there
    pass

def test_save_config_file(configuration_module):
    #podobnie jak wyzej
    pass

def test_put_settings_front(configuration_module):
    pass

def test_put_profile_to_front(current_profile):
    pass

def test_read_config_file(configuration_module):
    name = "zlanazwa"
    with pytest.raises(Exception) as e:
        configuration_module.read_config_file(name)
    assert e.type == FileNotFoundError
    name="dobranazwa"
    assert configuration_module.read_config_file(name) == 0