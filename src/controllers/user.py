from flask import json


class ControllerUser:
    def save(self, req):
        user = req.get_json()
        if user['name'] == "":
            return json.dumps({"code": 400, "description": "Você precisa preencher nome", }), 400
        elif user['cpf'] == "":
            return json.dumps({"code": 400, "description": "Você precisa preencher cpf", }), 400
        elif user['email'] == "":
            return json.dumps({"code": 400, "description": "Você precisa preencher email", }), 400
        elif user['cpf'] != "":
            return ""
        else:
            return json.dumps({"code": 200, "description": "Cadastro realizado com sucesso !!!", "data": user}), 200
