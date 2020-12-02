
import falcon

class GetFibonnaci(object):

    def on_get(self, req, resp, id):
        resp.body = id
        resp.status = falcon.HTTP_200
    