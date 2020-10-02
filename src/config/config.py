from flask import json

import json
from bson import ObjectId

import pymongo

URL = ""

client = pymongo.MongoClient(URL)
db = client["api"]
col = db["people"]


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class ConfigDB:
    """ CRIAR UM NOVO USUARIO """

    def save(self, user):
        userFilter = col.find_one({"cpf": user['cpf']})
        user = {'name': user['name'],
                'email': user['email'],
                'cpf': user['cpf'],
                'delete': False,
                'status': True}
        if userFilter == None:
            col.insert_one(user)
            return JSONEncoder().encode(user), 200
        else:
            return json.dumps({"code": 400, "description": "CPF já cadastrado no sistema", }), 400

    """ DELETAR UM USUARIO """

    def delete(self, user):
        userFilter = col.find_one({"cpf": user['cpf']})
        if userFilter == None:
            return json.dumps({"code": 400, "description": "Não foi possivel deletar essa conta", }), 400
        else:
            col.find_one_and_update(
                {'cpf': user['cpf']}, {'$set': {'delete': True, 'status': False}})
            return json.dumps({"code": 200, "description": "Usuario Deletado com Sucesso!!!", }), 200

    def query(self, user):
        newListUser = []
        for user in col.find({"$and": [{"delete": False}, {"status": True}, {"name": user['name']}, {"cpf": user['cpf']}, {"email": user['email']}]}):
            newListUser.append(user)
        return JSONEncoder().encode(newListUser), 200
