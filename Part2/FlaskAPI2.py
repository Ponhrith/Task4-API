from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

#create an endpoint


class Users(Resource):
    # methods go here
    #need to pass resource so that Flask knows that this class is an endpoint for the API
    pass

class Locations(Resource):
    pass

api.add_resource(Users, '/users')  # '/users' is our entry point, use api.add_resource to link the Users class with the /users endpoint
api.add_resource(Locations, '/location')

if __name__ == '__main__':
    app.run() #run the Flask app