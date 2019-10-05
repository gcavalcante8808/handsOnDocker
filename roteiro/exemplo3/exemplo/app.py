import falcon

from werkzeug.serving import run_simple

from middlewares.SQLAlchemyMiddleware import SQLAlchemySessionManager
from resources.Quotes import QuoteView
from resources.Index import IndexResource
from utils.db import setup_db


def create(db_connection_url, debug_sql=False):
    Session = setup_db(db_connection_url, debug_sql)
    db_session = SQLAlchemySessionManager(Session)

    quote_resource = QuoteView()
    index_resource = IndexResource()

    app = falcon.API(middleware=[db_session])
    app.add_route('/', index_resource)
    app.add_route('/quotes', quote_resource)
    return app


if __name__ == '__main__':
    app = create(db_connection_url='sqlite:////tmp/db.sqlite3')
    run_simple('0.0.0.0', 8000, app, use_reloader=True, use_debugger=True)
