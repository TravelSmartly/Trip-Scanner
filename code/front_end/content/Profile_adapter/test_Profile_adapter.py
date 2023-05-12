from code.front_end.content.Profile_adapter.Profile_adapter import Profile_adapter


def test_init():
    conf_module = Configuration_module()
    a = Profile_adapter(conf_module)

def test_download_categories():
    conf_module = None
    a = Profile_adapter(conf_module)
    dw_cat = a.download_categories()
    assert dw_cat == 0

def test_select_cat():
    conf_module = None
    a = Profile_adapter(conf_module)

    selected_id = 1
    s_cat = a.select_cat(selected_id)
    assert s_cat == 0

def test_select_cat2():
    conf_module = None
    a = Profile_adapter(conf_module)

    selected_id = "hi"
    s_cat = a.select_cat(selected_id)
    assert s_cat == 0

def test_deselect_cat():
    conf_module = None
    a = Profile_adapter(conf_module)

    selected_id = 1
    ds_cat = a.select_cat(selected_id)
    assert ds_cat == 0

def test_deselect_cat1():
    conf_module = None
    a = Profile_adapter(conf_module)

    selected_id = "hi"
    ds_cat = a.select_cat(selected_id)
    assert ds_cat == 0


def test_send_categories():
    conf_module = None
    a = Profile_adapter(conf_module)
    sd_cat = a.send_categories()
    assert sd_cat == 0


