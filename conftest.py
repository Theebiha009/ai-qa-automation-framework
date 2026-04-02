# conftest.py
import pytest
from api.client import APIClient
from config.config import BASE_URL, USERS

@pytest.fixture
def admin_client():
    client = APIClient()
    client.set_base_url(BASE_URL)
    client.login(**USERS["admin"])
    return client

@pytest.fixture
def shopper_client():
    client = APIClient()
    client.set_base_url(BASE_URL)
    client.login(**USERS["shopper"])
    return client

@pytest.fixture
def normal_client():
    client = APIClient()
    client.set_base_url(BASE_URL)
    client.login(**USERS["normal"])
    return client