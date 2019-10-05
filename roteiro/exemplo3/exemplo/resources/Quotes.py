from models.Quotes import Quote, QuoteSchema
from utils.logger import get_stream_logger

logger = get_stream_logger()


class QuoteView:

    def on_get(self, req, resp):
        db_objects = self.session.query(Quote).all()
        schema = QuoteSchema(session=self.session, many=True)

        logger.info(f'{len(db_objects)} quotes read.')

        result = schema.dump(db_objects)

        resp.media = result
