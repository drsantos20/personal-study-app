from main import app as my_app
import pytest


@pytest.yield_fixture
def app():
    yield my_app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))