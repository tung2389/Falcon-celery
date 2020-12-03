import falcon
import bcrypt
import jwt
from dotenv import load_dotenv
import os
import json
from model.user import UserModel

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

class Login(object):
    
    def on_get(self, req, resp):
        email = req.media['email']
        password = req.media['password']
        # Cannot use UserModel.objects(email = email).get here because get will raise an error if the user doesn't exist
        user = UserModel.objects(email = email)
        if not user:
            resp.status = falcon.HTTP_400
            resp.body = "Email or password is incorrent!"
            return

        user = user.get()
        if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
            jwtToken = jwt.encode(
                {'id': str(user.id)}, 
                JWT_SECRET, 
                algorithm='HS256'
            ).decode('utf-8')
            
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(
                {
                    'jwtToken': jwtToken, 
                    'message': "Logged in successfully!"
                }
            )
        else:
            resp.status = falcon.HTTP_400
            resp.body = "Email or password is incorrent!"