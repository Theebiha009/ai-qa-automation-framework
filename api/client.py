# api/client.py
import requests

class APIClient:
    def __init__(self):
        self.base_url = None
        self.session = requests.Session()
        self.token = None

    def set_base_url(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        url = f"{self.base_url}/auth"
        payload = {"username": username, "password": password}

        response = self.session.post(url, json=payload)
        print("Login Response:", response.text)
        assert response.status_code == 200, f"Login failed: {response.text}"

        self.token = response.json().get("token")
        assert self.token, "Token not received"
        self.session.headers.update({"Cookie": f"token={self.token}"})

    def get_bookings(self):
        url = f"{self.base_url}/booking"
        response = self.session.get(url)
        print("Bookings Response:", response.text)
        return response

    def create_booking(self, payload):
        url = f"{self.base_url}/booking"
        response = self.session.post(url, json=payload)
        print("Create Booking Response:", response.text)
        return response