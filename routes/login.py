import falcon
import bcrypt
from model.user import UserModel

class Login(object):
    
    def on_get(self, req, resp):
        email = req.media['email']
        password = req.media['password']
        if not UserModel.objects(email = email):
            resp.status = falcon.HTTP_400
            resp.body = "Email or password is incorrent!"
            return

        user = UserModel.objects(email = email).get()
        if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
            resp.status = falcon.HTTP_200
            resp.body = "Logged in successfully!"
        else:
            resp.status = falcon.HTTP_400
            resp.body = "Email or password is incorrent!"