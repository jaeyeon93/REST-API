# -*- coding: utf-8 -*-

from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')
    # this variable is a list of items
    # when we use lazy='dynamic' self.items is query?

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items':[item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        #this code is same as " select * from items where name=name LIMIT 1"
        # filter_by can use multiple argument, LIMIT 1 is only first row only

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

