import falcon
import bcrypt
from model.user import UserModel


class Signup(object):
    
    def on_post(self, req, resp):
        email = req.media['email']
        password = req.media['password']

        if not password:
            resp.status = falcon.HTTP_400
            resp.body = "Password cannot be emptied!"
            
        if not UserModel.objects(email = email):
            hashPassword = bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())
            newUser = UserModel(
                email = email,
                password = hashPassword
            )
            newUser.save()
            resp.status = falcon.HTTP_201
            resp.body = "Your account has been created!"
        else:
            resp.status = falcon.HTTP_400
            resp.body = "The email has been used!"
