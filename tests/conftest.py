import pytest 
from flasklate import create_app


@pytest.fixture
def test_client():
    app = create_app()

    test_client = app.test_client()
    context = app.app_context()
    context.push()

    yield test_client
    context.pop()