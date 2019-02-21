from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(40))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(100))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(500))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")



    def __repr__(self):
        return f'User {self.name}'

class Book(db.Model):
    __tablename__ = 'book'
    id= db.Column(db.Integer,primary_key = True)
    date = db.Column(db.String(100))
    resname= db.Column(db.String(40))
    restype = db.Column(db.String(30))
    adult= db.Column(db.Integer)
    children = db.Column(db.Integer) 
    
    @classmethod
    def get_book(cls,id):
        book = Book.query.filter_by(book_id=id).desc().all()
        return book



