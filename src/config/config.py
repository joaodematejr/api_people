from flask import json

import json
from bson import ObjectId

import pymongo

URL = "mongodb+srv://root:VAI_CRIAR_UMA_CONTA_PRA_VC@cluster0.aa4ya.mongodb.net/people?retryWrites=true&w=majority"

client = pymongo.MongoClient(URL)
db = client["api"]
col = db["people"]


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class ConfigDB:
    def save(self, user):
        user = {'name': user['name'],
                'email': user['email'],
                'cpf': user['cpf'],
                'delete': False,
                'status': True
                }
        col.insert_one(user)
        return JSONEncoder().encode(user), 200
