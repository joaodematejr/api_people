
from flask import Flask, request, json
from controllers.user import ControllerUser

userController = ControllerUser()


class Routes:
    def create(self, req):
        response = userController.save(req)
        return response
