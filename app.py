# -*- coding:utf-8 -*-

from flask import Flask #request
from flask_jwt import JWT #, jwt_required
from flask_restful import Api #, Resource,reqparse


from security import authenticate, identity
# resource는 api가 리턴하는 값들?로 생각할 수 있다
from resources.user import UserRegister
#resources.user  resources mean resource directory
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'jaeyeon'
api = Api(app)



jwt = JWT(app, authenticate, identity) # /auth
# jwt create an new endpoint?

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
