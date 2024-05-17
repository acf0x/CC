from pymongo import MongoClient, collection
from bson.json_util import dumps, loads

server = "localhost"
port = 27017
db = "northwind"

def Get_Customers_List() -> str:
    try:
        # return dumps(list(_Get_Collection("customers").find({}))
        return list(_Get_Collection("customers").find({}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}

def Get_Customer(id) -> str:
    try:
        # return dumps(_Get_Collection("customers").find_one({"CustomerID": id}))
        return _Get_Collection("customers").find_one({"CustomerID": id}, {"_id": 0})
    except Exception as e:
        return {"Error": e}

def _Get_Collection(collection, server=server, port=port, db=db):
    return MongoClient(f"mongodb://{server}:{port}/")[db][collection]


# PARA HCER


def Get_Orders_List() -> str:
    try:
        # return dumps(list(_Get_Collection("orders").find({}))
        return list(_Get_Collection("orders").find({}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}
    
def Get_Order(id) -> str:
    try:
        # return dumps(_Get_Collection("orders").find_one({"OrderID": id}))
        return _Get_Collection("orders").find_one({"OrderID": id}, {"_id": 0})
    except Exception as e:
        return {"Error": e}
    
    
def Get_Customer_Orders(id) -> list:
    try:
        # return dumps(list(_Get_Collection("orders").find_one({"CustomerID": id})))
        return list(_Get_Collection("orders").find({"CustomerID": id}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}