import falcon
import mongoengine as mongo

from routes.calcFibonnaci import CalcFibonnaci
from routes.getFibonnaci import GetFibonnaci

db = mongo.connect(
    "falcon-celery"
)
api = application = falcon.API()

calcFibonnaci = CalcFibonnaci()
getFibonnaci = GetFibonnaci()

api.add_route('/fibonnaci', calcFibonnaci)
api.add_route('/fibonnaci/{id}', getFibonnaci)