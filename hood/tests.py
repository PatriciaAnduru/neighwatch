from django.test import TestCase

from django.test import TestCase
from .models import *



class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):
        
        self.new_profile = Profile(user_id=2,hood_id=3,bio="just testing", email='patriciaanduru@gmail.com',name="Patricia",profile_pic="default.jpeg")

