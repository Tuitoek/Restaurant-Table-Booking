# from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
# from . import login_manager
from datetime import datetime

#login decorator modifies the loderuser function
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

#creating a class user and connecting the class to our database
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    stories = db.relationship('Stories',backref = 'user',lazy = "dynamic")
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")
   

    #this decorator generates my password and passes it to the passecurecolumn 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    #method that takes ,hashes and compares our password
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

#class stories  hosts user id, comments(relationship)
class Stories(db.Model):
    __tablename__='stories'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    category = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment',backref = 'stories',lazy = "dynamic")
    email = db.Column(db.String(255),unique = True,index = True)
 

    def save_stories(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_stories(cls,id):
        stories = Stories.query.all()
        return Stories

    def delete_stories(self):
        db.session.query(Stories).delete()
        db.session.commit()    

    def __repr__(self):
        return f'User {self.name}'        


#creating a class comment and connecting the class to comment on my stories
class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    stories_id = db.Column(db.Integer,db.ForeignKey('stories.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.all()
        return comments 

    def __repr__(self):
        return f'User {self.name}'


#class subscriber has column email for the user to receive an email after subscription
class Subscriber(db.Model):
    __tablename__="subscribers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)


    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls,id):
        return Subscriber.query.all()
         

    def __repr__(self):
        return f'User {self.email}'

