import os

import pytest
from ...app import create_app
import tempfile
from ..commands import init_test_db


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mktemp()

    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + db_path + ".sqlite",
        "WTF_CSRF_ENABLED": False,
        "DEBUG": False
    })

    with app.app_context():
        init_test_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
