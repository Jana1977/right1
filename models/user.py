import sqlite3

from db import db

#Has the USER CLASS and then the TWO methods to find a USER - when /AUTH is called with an USERNAME
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(80))
    password =db.Column(db.String(80))


    def __init__(self, username , password):
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from users where username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row is not None:
        #     user = cls(row[0], row[1], row[2])
        #     #user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from users where id=?"
        # result = cursor.execute(query,(_id,))
        # row = result.fetchone()
        # if row is not None:
        #     user = cls(row[0], row[1], row[2])
        #     #user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user