import falcon
from werkzeug.serving import run_simple

from middlewares.RedisCacheMiddleware import RedisCacheMiddleware
from middlewares.SQLAlchemyMiddleware import SQLAlchemySessionManager
from resources.Index import IndexResource
from resources.Quotes import QuoteView
from utils.cache import get_redis_conn
from utils.db import setup_db


def create(db_connection_url, debug_sql=False, cache_host='localhost', cache_port=6379, cache_db=0):
    Session = setup_db(db_connection_url, debug_sql)
    db_session_middleware = SQLAlchemySessionManager(Session)

    cache_conn_info = get_redis_conn(cache_host, cache_port, cache_db)
    cache_middleware = RedisCacheMiddleware(cache_conn_info)

    quote_resource = QuoteView()
    index_resource = IndexResource()

    app = falcon.API(middleware=[db_session_middleware, cache_middleware])
    app.add_route('/', index_resource)
    app.add_route('/quotes', quote_resource)
    return app


if __name__ == '__main__':
    app = create(db_connection_url='sqlite:////tmp/db.sqlite3',
                 debug_sql=False,
                 cache_host='localhost',
                 cache_port=6379,
                 cache_db=0)
    run_simple('0.0.0.0', 8000, app, use_reloader=True, use_debugger=True)
