from redis import Redis


def get_redis_conn(host='localhost', port='6379', db='0'):
    return Redis(host=host, port=port, db=db)
