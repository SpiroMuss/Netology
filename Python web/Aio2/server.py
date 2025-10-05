from aiohttp import web
import json
from sqlalchemy.exc import IntegrityError
from models import init_orm, close_orm, Advertisement, DbSession


async def orm_context(app: web.Application):
    await init_orm()
    print("START")
    yield
    await close_orm()
    print("FINISH")

def create_error(error_cls, error_message: str | dict | list):
    error = json.dumps({"error": error_message})
    return error_cls(
        text=error,
        content_type="application/json"
    )

@web.middleware
async def session_middleware(request: web.Request, handler):
    async with DbSession() as session:
        request.session = session
        result = await handler(request)
        return result


async def get_advertisement_by_id(session: DbSession, adv_id: int):
    adv = await session.get(Advertisement, adv_id)
    if adv is None:
        raise create_error(web.HTTPNotFound, "Advertisement not found")
    return adv

async def add_advertisement(session: DbSession, adv: Advertisement):
    try:
        session.add(adv)
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise create_error(web.HTTPConflict, "Advertisement already exists")


app = web.Application()
app.cleanup_ctx.append(orm_context)
app.middlewares.append(session_middleware)


class AdvView(web.View):

    @property
    def session(self) -> DbSession:
        return self.request.session

    @property
    def adv_id(self) -> int:
        return int(self.request.match_info(["adv_id"]))

    @property
    async def advertisement(self) -> Advertisement:
        return await get_advertisement_by_id(self.session, self.adv_id)


    async def get(self):
        adv = await self.advertisement
        return adv

    async def post(self):
        pass

    async def patch(self, adv_id):
        pass

    async def delete(self, adv_id):
        pass


app.add_routes([
    web.post(r"/advertisements/", AdvView),
    web.get(r"/advertisements/{adv_id: \d+}", AdvView),
    web.patch(r"/advertisements/{adv_id: \d+}", AdvView),
    web.delete(r"/advertisements/{adv_id: \d+}", AdvView),
])

web.run_app(app)