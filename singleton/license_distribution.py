from threading import Lock, Thread
from collections import defaultdict
import logging
import secrets
import string

class LicenseMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class LicenseDistribution(metaclass=LicenseMeta):
    total_licenses: int = 5
    license_tracker_dict: defaultdict = {}
    
    @classmethod
    def reset_instance(cls):
        cls._instances = {}
        cls.total_licenses = 5
        cls.license_tracker_dict = {}

    def __license_is_availible(self):
        license_is_availible = len(
            self.license_tracker_dict) < self.total_licenses
        return license_is_availible

    def __generate_license(self, user):
        N = 7
        license = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                          for i in range(N))
        self.license_tracker_dict[user] = license
        self.total_licenses -= 1 
        return license
    
    def __user_has_license(self, user):
        return user in self.license_tracker_dict

    def claim_license(self, user):
        license = None
        try:
            assert self.__license_is_availible() and not self.__user_has_license(user), 'user is not eligble to claim license'
            license = self.__generate_license(user)
        except AssertionError as e:
            raise AssertionError(e)
        return license
    
    def release_license(self, user):
        try:
            del self.license_tracker_dict[user]
            self.total_licenses += 1
        except Exception as e:
            raise Exception('Error releasing license for user')
    
    def get_license_count(self):
        return self.total_licenses

    def get_license_users(self):
        return self.license_tracker_dict.keys()

if __name__ == "__main__":
    license_obj = LicenseDistribution()

# tests -> single user should not be able to claim more than one license, unless priviledges are given 
# tests -> failure cases