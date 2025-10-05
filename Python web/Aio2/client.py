import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://0.0.0.0:8080/advertisements/1")
        print(await response.text())
        print(response.status)


asyncio.run(main())