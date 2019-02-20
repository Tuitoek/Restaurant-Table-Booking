import unittest
from app.models import User
from app import db

#the setup method creates an instances of our user
class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'manow',password = '1234', email = 'manowfelow@gmail.com')
        
        
    #saving my users to my database
    def save_user(self):
        db.session.add(self.new_user)
        db.session.commit()

    # this ascertains that our password is being hashed or not  
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    #this test confirms an error will occur when we try access password property
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    #tests that our password is being hashed
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('1234'))