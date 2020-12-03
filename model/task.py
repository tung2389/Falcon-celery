from mongoengine import *

class TaskModel(Document):
    _id = StringField(required = True, primary_key=True)
    result = LongField(required = True)
    meta = {'collection': 'task'}

