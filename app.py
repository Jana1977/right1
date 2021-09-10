import os

from flask import Flask, request
from flask_restful import Resource, Api

from flask_jwt import JWT , jwt_required
from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = 'jana2'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Setting this value to FALSE means we are turning OFF the FLASK's tracking capabilities and using the SQLALCHEMY's tracking capabilities.
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)




jwt = JWT(app, authenticate, identity)

usages = []

class Usage(Resource):
    @jwt_required()
    def get(self, username):
        usage = next(filter(lambda x: x['username'] == username, usages), None)
        return {'usage': usage}, 200 if usage else 404

    def post(self, username):
        if next(filter(lambda x: x['username'] == username, usages), None) is not None:
            return {'message': "This customer with username '{}' already exists.".format(username) } ,400

        data = request.get_json()
        #usage = {'emailorphone': emailorphone , '24_months_usage': 500  }
        usage = {'username': username, '24_months_usage': data['24_months_usage']}
        usages.append(usage)
        return usage  , 201

class AllUsages(Resource):
    def get(self):
        return {'allusages': usages}

class HomePage(Resource):
    def get(self):
        return {'utg_Home': "Welcome to Utg"}

api.add_resource(Usage, '/usage/<string:username>')
api.add_resource(AllUsages, '/usages')
api.add_resource(UserRegister, '/register')
api.add_resource(HomePage, '/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000 , debug=True)

