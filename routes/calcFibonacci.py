import falcon
from service.tasks import fibonacci

class CalcFibonacci(object):
    
    def on_post(self, req, resp):
        number = req.media['number']
        task = fibonacci.delay(int(number))
        resp.status = falcon.HTTP_200
        resp.body = task.id