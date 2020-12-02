import falcon
import jwt
from dotenv import load_dotenv
import os
from model.user import UserModel

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

class JWTAuthenticate(object):
    def process_request(self, req, resp):
        # Do not run this middleware on login or signup route
        if req.path != '/login' and req.path != 'signup':
            authorization = req.headers['AUTHORIZATION']
            # Authorization header has the form "Bearer jwtToken"
            jwtToken = authorization[7:]
            # If the signature is incorrect, jwt will raise an error, so better use try except here.
            try:
                data = jwt.decode(
                    jwtToken, 
                    JWT_SECRET, 
                    algorithms='HS256',
                )
                userId = data['id']
                if not UserModel.objects(id = userId):
                    resp.status = falcon.HTTP_401
                    resp.body = "Unauthorized request"
                    resp.complete = True

            except:
                resp.status = falcon.HTTP_401
                resp.body = "Unauthorized request"
                resp.complete = True
