import falcon
import mongoengine as mongo

from routes.calcFibonacci import CalcFibonacci
from routes.getFibonacci import GetFibonacci
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

calcFibonacci = CalcFibonacci()
getFibonacci = GetFibonacci()
login = Login()
signup = Signup()

api.add_route('/fibonacci', calcFibonacci)
# api.add_route('/fibonacci/{id}', getFibonacci)
api.add_route('/login/', login)
api.add_route('/signup/', signup)