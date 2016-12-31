# -*- coding: utf-8 -*-

# import sqlite3 we no longer need to sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) # precision is number of decimal point

    store_id = db.Column(db.Integer,db.ForeignKey('stores.id')) # In the stores.id of Foreignkey, stores is table name, id is column name
    # store_id를 통해 item들이 어느 store에 속해있는지 알 수 있다
    store = db.relationship('StoreModel')


    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price':self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first() #this code is same as " select * from items where name=name LIMIT 1"
        # filter_by can use multiple argument, LIMIT 1 is only first row only

        # """
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from items where name=?"
        # result = cursor.execute(query, (name, ))
        # row = result.fetchone()
        # connection.close()
        #
        # if row:
        #     return cls(*row)
        #     """
            #return cls(row[0], row[1])
            # row[0] means name, row[1] means price, cls[row[0],row[1] == class ItemModel: def __init__(self,name,price)


    def save_to_db(self):
        # role of save_to_db is saving model into databases
        # session is collection of object ....
        db.session.add(self)
        db.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "insert into items values (?, ?)"
        # # first means name second means price
        # cursor.execute(query, (self.name, self.price))
        #
        # connection.commit()
        # connection.close()


    def update(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "update items set price=? where name=?"
        # cursor.execute(query,(self.name, self.price))
        # connection.commit()
        # connection.close()
