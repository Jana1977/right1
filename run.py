from app import app
from db import db

db.init_app(app)


# the below 3 lines replaces the CREATE_TABLES.py - execution to create the USERS table
@app.before_first_request
def create_tables():
    db.create_all()