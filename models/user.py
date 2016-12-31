# -*- coding:utf-8 -*-
import sqlite3
from db import db

# User class doesn't belong to Resource Package
# Role of Model is helper to assist allow to find_name...more flexiblity in the program
class UserModel(db.Model):
    # this UserModel is a API but this isn't rest-api
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) # 80 characters maxmium
    password = db.Column(db.String(80))

    def __init__(self, username, password): # id is automatically generate
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # cls.query means "select * from users"



        # # cls is using current class
        # # def find_by_username(User, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # # (username,) can't understand
        # row = result.fetchone()
        # if row:
        #     user = cls(row[0], row[1], row[2])
        #     # user = User(row[0], row[1], row[2])
        #     # row[0] is first column id, row[1] is 2nd column username, row[2] is 3rd column password
        #     # each row matches __init__function argument
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # first id is column name, second id "_id" means value

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,)) # (username,)은 잘 이해가 안된다
        # row = result.fetchone()
        # if row:
        #     user = cls(row[0], row[1], row[2])
        #     # user = User(row[0], row[1], row[2])
        #     # row[0] is first column id, row[1] is 2nd column username, row[2] is 3rd column password
        #     # each row matches __init__function argument
        # else:
        #     user = None
        #
        # connection.close()
        # return user