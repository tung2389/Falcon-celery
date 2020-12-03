from mongoengine import *

class UserModel(Document):
    email = StringField(required = True)
    password = StringField(required = True)
    meta = {'collection': 'user'}

