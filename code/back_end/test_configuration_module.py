from configuration_module import Configuration_module
import pytest
import profile


@pytest.fixture
def configuration_module():
    return Configuration_module()


def test_start_configuration_module(configuration_module):
    #Does not return any specific objects, so just make sure that it returns 0 if succeeded
    test_configuration = configuration_module.Configuration_module()
    assert test_configuration.categories == None
    assert test_configuration.interval == 10
    assert test_configuration.first_timer == True
    assert test_configuration.proximity == 1
    assert test_configuration.start_configuration_module() == 0
    #name = "weird_name_that_doesnt_exist"
    #name = "config_file.cfg"

def test_save_profile(configuration_module):
    my_profile = profile.Profile("testing_profile", ["fitness", "cars"], 5, 2)
    test_configuration = configuration_module.Configuration_module()
    test_configuration.save_profile(my_profile)
    with open("config_file.cfg") as f:
        s_content_list = f.readlines()
        assert "testing_profile" in s_content_list[1]

def test_save_config_file(configuration_module):
    test_configuration = configuration_module.Configuration_module()
    my_profile = profile.Profile("testing_profile", ["fitness", "cars"], 5, 2)
    my_profile2 = profile.Profile("testing_profile2", ["hotels_apartements", "restaurants"], 4, 1)
    map_object0 = {"id": 334234, "name": "a Grande Mamma", "category": None,
                       "coordinates": (50.06163905474776, 19.936530642326513), "description": None,
                       "rating": None}  # Set fixed existing objects
    map_object1 = {"id": 43243, "name": "Aparthotel Stare Miasto", "category": None,
                       "coordinates": (50.06182501735149, 19.933510474939244), "description": None, "rating": (4.2, 60)}
    my_favourites = {"testing_profile": [map_object0, map_object1]}
    my_favourites2 = {"testing_profile2": []}
    settings = {"night_mode": False} #settings may be modified/changed in the future versions
    input_tuple = (settings, [my_profile, my_profile2], [my_favourites, my_favourites2])
    test_configuration.save_config_file (input_tuple)
    with open("config_file.cfg") as f:
        s_content_list = f.readlines()
        assert "False" in s_content_list[0] #False means it is not the "welcome" screen, so we want this to be found in config_file after saving
        assert "testing_profile" in s_content_list[1]
        assert "testing_profile2" in s_content_list[1]
        assert "night_mode: False" in s_content_list[2]
        assert "testing_profile" in s_content_list[3]
        assert "testing_profile2" in s_content_list[3]
    

def test_put_settings_front(configuration_module):
    test_configuration = configuration_module.Configuration_module()
    my_profile = profile.Profile("testing_profile", ["fitness", "cars"], 5, 2)
    my_favourites2 = {"testing_profile2": []}
    settings = {"night_mode": False} #settings may be modified/changed in the future versions
    input_tuple = (settings, [my_profile], [my_favourites2])
    test_configuration.save_config_file (input_tuple)
    assert test_configuration.put_settings_front() == settings

### Very simple tests, just to see if this static/or outside method doesnt break on basic/void data
def test_put_profile_to_front(configuration_module):
    test_configuration = configuration_module.Configuration_module()
    my_profile = profile.Profile("testing_profile", ["fitness", "cars", "markets"], 3, 3)
    my_profile = profile.Profile("testing_profile2", ["markets"], 1, 1)
    my_profile = profile.Profile("testing_profile3", [], 2, 5)
    assert test_configuration.put_profile_to_front(my_profile) == my_profile
    assert test_configuration.put_profile_to_front(my_profile2) == my_profile2
    assert test_configuration.put_profile_to_front(my_profile3) == my_profile3

def test_read_config_file(configuration_module):
    name = "zlanazwa"
    with pytest.raises(Exception) as e:
        configuration_module.read_config_file(name)
    assert e.type == FileNotFoundError
    name="dobranazwa"
    assert configuration_module.read_config_file(name) == 0
