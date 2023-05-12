from code.front_end.content.Map_data_adapter.User_location_adapter import User_location_adapter

def test_init():
    loc_module = Location_module()
    a = User_location_adapter(loc_module)


def test_download_location():
    loc_module = None
    a = User_location_adapter(loc_module)
    dl = a.download_location()
    assert dl == 0


def test_location_postprocessing():
    loc_module = None
    a = User_location_adapter(loc_module)
    dl = a.location_postprocessing()
    assert dl == 0

def test_get_curr_location():
    loc_module = None
    a = User_location_adapter(loc_module)
    data = a.get_curr_location()
    assert len(data) != 0



