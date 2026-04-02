# tests/test_booking.py
import pytest
from api.client import APIClient
from utils.logger import log_json
from utils.schema_utils import validate_schema


# tests/test_booking.py
def test_get_bookings(normal_client):
    response = normal_client.get_bookings()
    if response.status_code != 200:
        log_json({
            "test_name": "test_get_bookings",
            "api": "booking",
            "status_code": response.status_code,
            "error_type": "status_code",
            "message": response.text
        })
    assert response.status_code == 200
    print("Bookings:", response.json())
    # Validate JSON schema
    #validate_schema(response.json(), "booking_schema.json")

def test_create_booking(normal_client):
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-05"},
        "additionalneeds": "Breakfast"
    }
    response = normal_client.create_booking(payload)
    assert response.status_code == 200
    data = response.json()
    assert "bookingid" in data
    print("Created Booking:", data)