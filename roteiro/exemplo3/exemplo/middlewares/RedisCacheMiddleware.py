class RedisCacheMiddleware:
    def __init__(self, Session):
        self.session = Session

    def process_resource(self, req, resp, resource, params):
        resource.cache_session = self.session
