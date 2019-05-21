from app import db
from datetime import datetime
from werkzeug.security import  generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin,db.Model):
    __tablename__="user"
    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(64),index = True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post",backref="author",lazy="dynamic")

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return "<用户名:{}>".format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    __tablename__= "post"
    id = db.Column(db.Integer,primary_key= True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Post {}>".format(self.body)

class Books(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer,primary_key=True)
    bookname = db.Column(db.String(32))
    author = db.Column(db.String(32))
    bookpath = db.Column(db.String(128),unique=True)

    def __repr__(self):
        return "<Book {}>".format(self.bookpath)

class Booksection(db.Model):
    __tablename__ = "booksection"
    section_id = db.Column(db.Integer,primary_key=True)
    section_name = db.Column(db.String(64))
    section_path = db.Column(db.String(128))
    book_id = db.Column(db.Integer,db.ForeignKey("books.id"))

    def __repr__(self):
        return "<Section {}>".format(self.section_id)
