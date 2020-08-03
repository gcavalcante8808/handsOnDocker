from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def setup_db(db_connection_url, sql_debug=False):
    engine = create_engine(
        db_connection_url,
        echo=sql_debug
    )

    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)
    
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    return Session
