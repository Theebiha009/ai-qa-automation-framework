import pytest
from utils.helpers import load_csv_data, build_payload

data = load_csv_data("data/booking_data.csv")

@pytest.mark.parametrize("booking_data", data)
def test_create_booking_csv(normal_client, booking_data):
    payload = build_payload(booking_data)

    response = normal_client.create_booking(payload)

    assert response.status_code == 200