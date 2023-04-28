import pytest
from Profile_adapter import Profile_adapter


def test_init():
    conf_module = Configuration_module()
    a = Profile_adapter(conf_module)

def test_download_categories():
    conf_module = None
    a = Profile_adapter(conf_module)
    a.download_categories()

