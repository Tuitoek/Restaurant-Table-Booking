import unittest
from app.models import Subscriber
from app import db

#the setup method creates an instances of our user
class SubscriberModelTest(unittest.TestCase):
    def setUp(self):
        self.new_subscriber = Subscriber(name = 'manow',title = '1234', email = 'manowfelow@gmail.com')
        
        
    #saving my users to my database
    def save_subscriber(self):
        db.session.add(self.new_subscriber)
        db.session.commit()