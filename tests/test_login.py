import requests
from utils.logger import log_json

def test_login(normal_client):
    try:
        response = normal_client.get_bookings()

        assert response.status_code == 200

    except requests.exceptions.Timeout:
        log_json({
            "test_name": "test_login",
            "api": "login",
            "error_type": "timeout",
            "message": "Request timed out"
        })
        raise