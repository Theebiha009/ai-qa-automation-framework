import asyncio
import aiohttp
import uuid

from api.async_client import AsyncAPIClient
from utils.helpers import load_json_data, build_payload

data = load_json_data("data/booking_data.json")


async def create_all_bookings():
    client = AsyncAPIClient("https://restful-booker.herokuapp.com")

    async with aiohttp.ClientSession() as session:
        tasks = []

        for d in data:
            # ✅ make data unique
            d["firstname"] += str(uuid.uuid4())[:5]

            payload = build_payload(d)

            tasks.append(client.create_booking(session, payload))

        results = await asyncio.gather(*tasks)

        return results


def test_create_booking_async():
    results = asyncio.run(create_all_bookings())

    for res, status in results:
        print(res)
        assert status == 200