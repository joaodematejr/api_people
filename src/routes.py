
from flask import Flask, request, json
from controllers.user import ControllerUser

user = ControllerUser()


class Routes:
    def user_create(self, req):
        response = user.save(req)
        return response
