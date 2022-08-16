import pytest 
from project import app


@pytest.fixture
def test_client():
    test_client = app.test_client()
    context = app.app_context()
    
    context.push()

    yield test_client

    context.pop()