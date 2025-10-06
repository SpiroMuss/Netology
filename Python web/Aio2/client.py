import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:

        # response = await session.get("http://localhost:8080/advertisements/3")

        response = await session.post("http://localhost:8080/advertisements/",
                                      json={
                                          "header": "Header",
                                          "comment": "Comment",
                                          "owner": "Owner",
                                      })

        # response = await session.patch("http://localhost:8080/advertisements/1",
        #                                json={
        #                                    "header": "HEADER",
        #                                })

        # response = await session.delete("http://localhost:8080/advertisements/1")

        print(await response.text())


asyncio.run(main())