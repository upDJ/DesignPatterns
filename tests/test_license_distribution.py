from singleton import LicenseDistribution
import pytest

obj = LicenseDistribution()
def test_obj_instance():
    assert isinstance(obj, LicenseDistribution)

def test_valid_license_claim():  
    valid_license = obj.claim_license(user='john')
    assert valid_license

def test_invalid_license_claim():
    with pytest.raises(Exception):
        valid_license = obj.claim_license(user='john')

    