import pytest
import requests

class APIClient:
    BASE_URL = "http://example.com"  # Replace with your actual API base URL

    @staticmethod
    def create_booking(data):
        response = requests.post(f"{APIClient.BASE_URL}/booking", json=data)
        return response


@pytest.mark.parametrize("data, expected_status", [
    (
        {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-01-01",
                "checkout": "2023-01-10"
            },
            "additionalneeds": "Breakfast"
        },
        200
    ),
    (
        {
            "firstname": "Jane",
            "lastname": "Smith",
            "totalprice": 150,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2023-01-05",
                "checkout": "2023-01-15"
            },
            "additionalneeds": ""
        },
        200
    ),
    (
        {
            "firstname": "",
            "lastname": "Johnson",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-02-01",
                "checkout": "2023-02-02"
            },
            "additionalneeds": "Late checkout"
        },
        400
    ),
    (
        {
            "firstname": "Emily",
            "lastname": "White",
            "totalprice": -50,  # Invalid total price
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-02-10",
                "checkout": "2023-02-12"
            },
            "additionalneeds": "WiFi"
        },
        400
    ),
    (
        {
            "firstname": "Michael",
            "lastname": "Brown",
            "totalprice": 300,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-02-20",
                "checkout": "2023-02-22"
            },
            "additionalneeds": None  # Invalid additional needs
        },
        400
    )
])
def test_create_booking(data, expected_status):
    response = APIClient.create_booking(data)
    assert response.status_code == expected_status

    if expected_status == 200:
        response_data = response.json()
        assert "bookingid" in response_data
        assert response_data["booking"]["firstname"] == data["firstname"]
        assert response_data["booking"]["lastname"] == data["lastname"]
        assert response_data["booking"]["totalprice"] == data["totalprice"]
        assert response_data["booking"]["depositpaid"] == data["depositpaid"]
        assert response_data["booking"]["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
        assert response_data["booking"]["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]