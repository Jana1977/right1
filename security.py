# these TWO methods are here for the /auth endpoint

from models.user import UserModel
from werkzeug.security import safe_str_cmp


# users = [
#     User(1, 'jana@gmail.com' , '1234' ),
#     User(2, 'kavi@gmail.com' , 'asdf' ),
#     User(3, 'jana' , 'test' ),
# ]
#
# username_mapping = {u.username: u for u in users}
# id_mapping = {u.id: u for u in users }

def authenticate(username , password):
    # user =  username_mapping.get(username, None)
    #if user is not None and safe_str_cmp(user.password, password):
    user =  UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password , password ):
        print("yes matched")
        return user

def identity(payload):
    user_id = payload['identity']
    print('user_id - > ', user_id)
    return UserModel.find_by_userid(user_id)
    # return id_mapping.get(user_id, None)