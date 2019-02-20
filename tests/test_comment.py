import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_manow = User(username = 'manow',password = '1234')
        self.new_comment = Comment(description='comments',user = self.user_manow)

    # def tearDown(self):
    #         Review.query.delete()
    #         User.query.delete()

    
    def test_check_instance_variable(self):
        self.assertEquals(self.new_comment.description,'cat')
                
        # self.assertEquals(self.new_comment.user,self.user_manow)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1234)
        self.assertTrue(len(got_comments) == 1) 