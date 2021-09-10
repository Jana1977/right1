import sqlite3
from flask_restful import Resource , reqparse
from models.user import UserModel

# Class called for USER REGISISTRATION via end point /register
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"messages":"User Already exists"}, 400

        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # insert_query = "Insert into users values (Null , ? ,? )"
        # cursor.execute(insert_query, (data["username"], data["password"],))
        # connection.commit()
        # connection.close()

        return {"message": "User Created Successfully"}, 201
