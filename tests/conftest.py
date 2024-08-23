from server.app import create_app
import pytest
from server.config.config_test import SQLALCHEMY_DATABASE_URI


@pytest.fixture(scope="module")
def client(request):
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": SQLALCHEMY_DATABASE_URI})
    test_client = app.test_client()
    app.app_context().push()
    yield test_client
