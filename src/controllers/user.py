from flask import json


from config.config import ConfigDB
from utils.utils import Utils

database = ConfigDB()
utils = Utils()


class ControllerUser:
    def save(self, req):
        user = req.get_json()
        if user['name'] == "":
            return json.dumps({"code": 400, "description": "Você precisa preencher nome, seu burro!", }), 400
        elif len(user['name']) > 150:
            return json.dumps({"code": 400, "description": "Nome não pode utrapassar 150 caracteres, você não sabe contar idiota!", }), 400
        elif user['cpf'] == "":
            return json.dumps({"code": 400, "description": "Você precisa preencher cpf! idiotaa", }), 400
        elif user['email'] == "":
            return json.dumps({"code": 400, "description": "Você precisa preencher email, idiota!", }), 400
        elif len(user['email']) > 400:
            return json.dumps({"code": 400, "description": "Email não pode utrapassar 400 caracteres, pra que um email com mais de 400 caracteres idiota!", }), 400
        elif user['cpf'] != "":
            response = utils.validar_cpf(user['cpf'])
            if response == False:
                return json.dumps({"code": 400, "description": "CPF invalido, é pra colocar um cpf valido imbecil!", }), 400
            else:
                if user['email'] != "":
                    responseEmail = utils.validar_email(user['email'])
                    if responseEmail == False:
                        return json.dumps({"code": 400, "description": "Email invalido, é pra colocar um email valido imbecil!", }), 400
                    else:
                        return database.save(user)

    def remove(self, req):
        user = req.get_json()
        if user['cpf'] == None:
            return json.dumps({"code": 400, "description": "CPF invalido, é pra colocar um cpf valido imbecil!", }), 400
        else:
            return database.delete(user)

    def query(self, req):
        user = req.get_json()
        return database.query(user)
