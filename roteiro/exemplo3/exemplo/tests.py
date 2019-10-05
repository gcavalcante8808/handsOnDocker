
from falcon import testing
from models.Quotes import Quote
from utils.db import setup_db
from utils.logger import get_test_logger

import os
import pytest

import app


@pytest.fixture()
def client():
    return testing.TestClient(app.create(db_connection_url='sqlite:////tmp/tests.sqlite3'))


@pytest.fixture()
def db_session():
    return setup_db(db_connection_url='sqlite:////tmp/tests.sqlite3')


@pytest.fixture()
def remove_db_files():
    yield
    os.remove('/tmp/tests.sqlite3')


def _save_sqlalchemy_object(obj, db_session):
    db_session.add(obj)
    db_session.commit()


def test_get_index(client):
    doc = {'message': 'Nothing is Easy!'}

    result = client.simulate_get('/')
    assert result.status_code == 200
    assert result.json == doc


def test_list_quotes(client, db_session, remove_db_files):
    quote = Quote()
    quote.quote = "shu"
    _save_sqlalchemy_object(quote, db_session)

    result = client.simulate_get('/quotes')

    assert result.json
    assert len(result.json) == 1
    return_quote = result.json[0]
    assert 'id' in return_quote
    assert 'quote' in return_quote
    assert return_quote.get('quote') == quote.quote


def test_generate_logs_when_a_client_retrieves_quotes(client):
    logger = get_test_logger()

    client.simulate_get('/quotes')

    assert hasattr(logger.handlers[0], 'last_message')
    assert '0 quotes read.' in logger.handlers[0].last_message
