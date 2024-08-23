from server.app import create_app
from server.db import db
from server.init_db import init_db
import pytest
from server.config.config_test import SQLALCHEMY_DATABASE_URI


@pytest.fixture(scope="module")
def client(request):
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": SQLALCHEMY_DATABASE_URI})
    test_client = app.test_client()
    app.app_context().push()
    yield test_client
