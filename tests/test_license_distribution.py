from singleton import LicenseDistribution
import pytest

obj = LicenseDistribution()
def test_obj_instance():
    assert isinstance(obj, LicenseDistribution)

def test_valid_license_claim():  
    valid_license = obj.claim_license(user='test')
    assert valid_license

def test_valid_license_count(n=1):
    valid_license = obj.claim_license(user='test')
    assert obj.get_license_count() == n

def test_release_license_by_user(user='test'):
    obj.claim_license(user=user)
    obj.release_license(user=user)
    assert user not in obj.get_license_users()

def test_invalid_license_claim_user_has_open_license():
    obj.claim_license(user='test')
    with pytest.raises(Exception):
        obj.claim_license(user='test')

def test_invalid_release_license(user='test'):
    with pytest.raises(Exception):
        obj.release_license(user=user)