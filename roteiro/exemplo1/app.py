from werkzeug.serving import run_simple

import falcon


class IndexResource:
    def on_get(self, req, resp):
        message = {'message': 'Nothing is Easy!'}

        resp.media = message


def create():
    return falcon.API()

if __name__ == '__main__':
    app = create()
    run_simple('0.0.0.0', 8000, app, use_reloader=True, use_debugger=True)
