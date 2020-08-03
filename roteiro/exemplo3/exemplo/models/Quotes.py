
from sqlalchemy import Column, Integer, String, ForeignKey,Float
from marshmallow_sqlalchemy import ModelSchema

from utils.db import Base


class Quote(Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True)
    quote = Column(String, nullable=False)


class QuoteSchema(ModelSchema):
    class Meta:
        model = Quote
