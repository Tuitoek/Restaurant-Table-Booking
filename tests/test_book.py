import unittest
from app.models import Book,User
from app import db

class BookModelTest(unittest.TestCase):
    def setUp(self):
        self.user_manow = User(username = 'manow',password = '1234')
        self.new_book = Book(id=1,date='28/02/2018',resname='Manow',restype ='single', adult=3,children=4)

    def test_check_instance_variable(self):
        self.assertEquals(self.new_book.id,1)
        self.assertEquals(self.new_book.date,'28/02/2018')
        self.assertEquals(self.new_book.resname,'Manow')
        self.assertEquals(self.new_book.restype, 'single')
        self.assertEquals(self.new_book.adult, 3)
        self.assertEquals(self.new_book.children, 4)
      

    def test_get_book_by_id(self):
        got_book = Book.get_book(12345)
        self.assertTrue(len(got_book) > 0) 