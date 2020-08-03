
from falcon import testing
import pytest

@pytest.fixture()
def client():
    return testing.TestClient(app.create())


def test_get_index(client):
    doc = {'message': 'Nothing is Easy!'}

    result = client.simulate_get('/')
    assert result.status == 200
    assert result.json == doc
