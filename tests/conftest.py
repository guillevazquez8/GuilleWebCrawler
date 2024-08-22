from server.app import app
from server.db import db
import pytest


@pytest.fixture(scope="module")
def client(request):
    app.config.from_pyfile("config/config_test.py")
    test_client = app.test_client()
    app.app_context().push()
    db.drop_all()
    db.create_all()

    def tearDown():
        app.app_context().push()
        db.drop_all()

    request.addfinalizer(tearDown)
    return test_client
