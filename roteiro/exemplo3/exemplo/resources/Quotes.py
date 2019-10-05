from models.Quotes import Quote, QuoteSchema


class QuoteView:

    def on_get(self, req, resp):
        db_objects = self.session.query(Quote).all()
        schema = QuoteSchema(session=self.session, many=True)

        result = schema.dump(db_objects)

        resp.media = result
