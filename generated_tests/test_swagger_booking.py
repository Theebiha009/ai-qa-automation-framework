import pytest
import requests

class APIClient:
    BASE_URL = "http://example.com"  # Replace with the actual base URL

    @staticmethod
    def create_booking(data):
        response = requests.post(f"{APIClient.BASE_URL}/booking", json=data)
        return response


@pytest.fixture
def booking_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-01",
            "checkout": "2023-10-10"
        },
        "additionalneeds": "Breakfast"
    }

def test_create_booking_success(booking_data):
    response = APIClient.create_booking(booking_data)
    
    assert response.status_code == 200
    response_json = response.json()
    assert "bookingid" in response_json
    assert response_json["booking"]["firstname"] == booking_data["firstname"]
    assert response_json["booking"]["lastname"] == booking_data["lastname"]
    assert response_json["booking"]["totalprice"] == booking_data["totalprice"]
    assert response_json["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response_json["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response_json["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]

def test_create_booking_missing_firstname():
    booking_data = {
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-01",
            "checkout": "2023-10-10"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = APIClient.create_booking(booking_data)
    
    assert response.status_code == 400
    assert response.json().get("error") == "Firstname is required"

def test_create_booking_invalid_dates(booking_data):
    booking_data["bookingdates"]["checkin"] = "2023-10-10"
    booking_data["bookingdates"]["checkout"] = "2023-10-01"
    
    response = APIClient.create_booking(booking_data)
    
    assert response.status_code == 400
    assert response.json().get("error") == "Checkout date must be after checkin date"

def test_create_booking_missing_totalprice(booking_data):
    booking_data["totalprice"] = None
    
    response = APIClient.create_booking(booking_data)
    
    assert response.status_code == 400
    assert response.json().get("error") == "Total price must be a valid number"