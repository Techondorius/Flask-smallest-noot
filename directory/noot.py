import sys
sys.dont_write_bytecode = True

from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Blueprint('noot', __name__)
api = Api(app)

class Noot(Resource):
    def get(self):
        return {"message":"got noot"}

api.add_resource(Noot, "/noot")