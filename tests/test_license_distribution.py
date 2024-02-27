from singleton import LicenseDistribution
import pytest

@pytest.fixture(scope='function')
def reset_license_singleton():
    # setup code here
    yield
    # teardown code here
    LicenseDistribution.reset_instance()

def test_obj_instance():
    obj = LicenseDistribution()
    assert isinstance(obj, LicenseDistribution)

def test_valid_license_claim(reset_license_singleton):
    
    obj = LicenseDistribution()  
    valid_license = obj.claim_license(user='test')
    assert valid_license

def test_valid_license_count(reset_license_singleton):
    obj = LicenseDistribution()
    valid_license = obj.claim_license(user='test')
    assert obj.get_license_count() == 4

def test_release_license_by_user(reset_license_singleton, user='test'):
    obj = LicenseDistribution()
    obj.claim_license(user=user)
    obj.release_license(user=user)
    assert user not in obj.get_license_users()

def test_invalid_license_claim_user_has_open_license(reset_license_singleton):
    obj = LicenseDistribution()
    obj.claim_license(user='test')
    with pytest.raises(AssertionError):
        obj.claim_license(user='test')

def test_invalid_release_license(reset_license_singleton, user='test'):
    obj = LicenseDistribution()
    with pytest.raises(Exception):
        obj.release_license(user=user)