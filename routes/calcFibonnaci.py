import falcon

class CalcFibonnaci(object):
    
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200