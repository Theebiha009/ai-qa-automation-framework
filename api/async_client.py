import aiohttp

class AsyncAPIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    async def create_booking(self, session, payload):
        url = f"{self.base_url}/booking"

        async with session.post(url, json=payload) as response:
            return await response.json(), response.status