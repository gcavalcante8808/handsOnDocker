

class IndexResource:
    def on_get(self, req, resp):
        message = {'message': 'Nothing is Easy!'}

        resp.media = message
