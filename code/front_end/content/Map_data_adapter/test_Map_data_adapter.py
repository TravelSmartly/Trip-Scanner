from code.front_end.content.Map_data_adapter.Map_data_adapter import Map_data_adapter


def test_init():
    ar_module = Arranging_module()
    a = Map_data_adapter(ar_module)

def test_download_places():
    ar_module = None
    a = Map_data_adapter(ar_module)
    dl_pl = a.download_places()
    assert dl_pl == 0


def test_data_postprocessing():
    ar_module = None
    a = Map_data_adapter(ar_module)
    dl_pl = a.data_postprocessing()
    assert dl_pl == 0


def test_get_places_data():
    ar_module = None
    a = Map_data_adapter(ar_module)
    places = a.get_places_data()
    assert len(places) != 0


