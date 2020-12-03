
import falcon

class GetFibonacci(object):

    def on_get(self, req, resp, taskId):
        with open("data.txt", "r") as dataFile:
            for line in dataFile:
                if line.split()[0] == taskId:
                    resp.status = falcon.HTTP_200
                    resp.body = line.split()[2]
                    return
                else:
                    resp.status = falcon.HTTP_404
                    resp.body = "not available"
                
    