import pytest
from utils.helpers import load_json_data, build_payload

data = load_json_data("data/booking_data.json")

@pytest.mark.parametrize("booking_data", data)
def test_create_booking_json(normal_client, booking_data):
    payload = build_payload(booking_data)

    response = normal_client.create_booking(payload)

    assert response.status_code == 200

    res_data = response.json()

    assert res_data["booking"]["firstname"] == booking_data["firstname"]
    assert res_data["booking"]["lastname"] == booking_data["lastname"]