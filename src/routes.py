
from flask import Flask, request, json
from controllers.user import User

user = User()


class Routes:
    def user_create(self, req):
        response = user.save(req)
        return response
