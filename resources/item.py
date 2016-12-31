# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                            required=True,
                            help="This field cannot be left blank!"
    )

    parser.add_argument('store_id',
                        type=int,
                            required=True,
                            help="Every item needs a store id"
    )


    @jwt_required()
    def get(self , name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item not found'},404


    def post(self,name):
        if ItemModel.find_by_name(name):
        #self.get called jwt tokken
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name,**data)
        #item = ItemModel(name,data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
            # 500 is Internal Server Error
        return item.json(), 201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "delete from items where name=?" # name=?이 없으면 모두 다 지워진다
        # cursor.execute(query, (name,))
        # connection.commit()
        # connection.close()

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data) # this is simplify code of under code
            #item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()

        # item is one of we found the database.
        #updated_item = ItemModel(name, data['price'])
        # updated_item is a new item. that's not in database. we just created
        # if item is None:
        #     try:
        #         updated_item.insert()
        #     except:
        #         return {"message": "An error occurred updating the item."}, 500
        # else:
        #     try:
        #         updated_item.update()
        #     except:
        #         return {"message": "An error occurred updating the item."}, 500
        # return updated_item.json()

class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
        # 2.return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        # 1. return {'items': item.json() for item in ItemModel.query.all()}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0],'price':row[1]})
        #
        # connection.commit()
        # connection.close()
        # return {'items':items}
        # # second items is items = []