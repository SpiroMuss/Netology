import asyncio

import aiohttp
from more_itertools import chunked

from models import init_orm, close_orm, DbSession, SWCharacter

MAX_REQUESTS = 10


async def get_character(char_id: int, session):
    response = await session.get(f"https://www.swapi.tech/api/people/{char_id}")
    json_data = await response.json()
    if json_data['message'] != "ok":
        return {'status': 'error'}
    else:
        char_info = json_data['result']['properties']

        result = {
            'status': 'ok',
            'birth_year': char_info['birth_year'],
            'eye_color': char_info['eye_color'],
            'gender': char_info['gender'],
            'hair_color': char_info['hair_color'],
            'homeworld': char_info['homeworld'],
            'mass': char_info['mass'],
            'name': char_info['name'],
            'skin_color': char_info['skin_color'],
        }

        return result


async def save_characters(characters_info: list[dict]):
    async with DbSession() as session:
        orm_objects = [SWCharacter(
            birth_year=char['birth_year'] if char['birth_year'] != ('unknown' or 'n/a') else None,
            eye_color=char['eye_color'] if char['eye_color'] != ('unknown' or 'n/a') else None,
            gender=char['gender'] if char['gender'] != ('unknown' or 'n/a') else None,
            hair_color=char['hair_color'] if char['hair_color'] != ('unknown' or 'n/a') else None,
            homeworld=char['homeworld'] if char['homeworld'] != ('unknown' or 'n/a') else None,
            mass=char['mass'] if char['mass'] != ('unknown' or 'n/a') else None,
            name=char['name'] if char['name'] != ('unknown' or 'n/a') else None,
            skin_color=char['skin_color'] if char['skin_color'] != ('unknown' or 'n/a') else None,
        ) for char in characters_info if char['status'] == 'ok']
        session.add_all(orm_objects)
        await session.commit()


async def main():
    await init_orm()

    async with aiohttp.ClientSession() as http_session:
        response = await http_session.get("https://www.swapi.tech/api/people")
        people_count = (await response.json())["total_records"]

        for chunk in chunked(range(1, people_count + 1), MAX_REQUESTS):
            coros = [get_character(char_id, session=http_session) for char_id in chunk]
            characters_info = await asyncio.gather(*coros)
            save_task = asyncio.create_task(save_characters(characters_info))

    tasks = asyncio.all_tasks()
    current_task = asyncio.current_task()
    tasks.remove(current_task)
    for task in tasks:
        await task

    await close_orm()

asyncio.run(main())