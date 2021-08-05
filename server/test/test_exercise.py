from ..util import get_fixture
from flask.testing import FlaskClient
import json
import pytest
import random

from ..lib.app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})

    with app.test_client() as client:
        yield client


def test_get(client: FlaskClient):
    res = client.get(f"/exercise/{random.randint(0,100)}")
    assert json.loads(res.data) == get_fixture("exercise")
