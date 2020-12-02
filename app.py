import falcon
import mongoengine as mongo

from routes.calcFibonnaci import CalcFibonnaci
from routes.getFibonnaci import GetFibonnaci
from routes.login import Login
from routes.signup import Signup

from middleware.jwtAuthenticate import JWTAuthenticate

db = mongo.connect(
    "falcon-celery"
)
api = application = falcon.API(
    middleware = [
        JWTAuthenticate()
    ]
)

calcFibonnaci = CalcFibonnaci()
getFibonnaci = GetFibonnaci()
login = Login()
signup = Signup()

api.add_route('/fibonnaci', calcFibonnaci)
api.add_route('/fibonnaci/{id}', getFibonnaci)
api.add_route('/login/', login)
api.add_route('/signup/', signup)