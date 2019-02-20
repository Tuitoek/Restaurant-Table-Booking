import unittest
from app.models import Stories,User,Pitch
from app import db

class StoriesModelTest(unittest.TestCase):
    def setUp(self):
        self.user_manow = User(username = 'manow',password = '1234')
        self.new_stories = Stories(name='cat',title='movie',description='moviereview',user =self.user_manow, category='technology')

    # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()

    def test_check_instance_variable(self):
        self.assertEquals(self.new_stories.name,'cat')
        self.assertEquals(self.new_stories.title,'movie')
        self.assertEquals(self.new_stories.description,'moviereview')
        self.assertEquals(self.new_stories.category, 'technology')
        # self.assertEquals(self.new_pitch.user,self.user_manow)  

    def test_save_stories(self):
        self.new_stories.save_stories()
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_stories_by_id(self):
        self.new_stories.save_stories()
        got_stories = Stories.get_stories(12345)
        self.assertTrue(len(got_stories) > 0) 