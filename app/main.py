import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.views import (
    AboutUsAdmin,
    MainContentAdmin,
    NewsAdmin,
    NewsImagesAdmin,
    PriceListAdmin,
    ProductsAdmin,
    ProductsImagesAdmin,
    ProductsInfoAdmin,
    TextPagesAdmin,
    UsersAdmin,
)
from app.config import settings
from app.database import engine
from app.logger import logger
from app.main_content.router import router as content_router
from app.news.router import router as news_router
from app.pages.router import router as pages_router
from app.products.router import router as products_router
from app.text_pages.router import router as text_pages_router
from app.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # при запуске
    redis = aioredis.from_url(
        settings.REDIS_URL,
        encoding="utf8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield
    # при выключении


app = FastAPI(
    title="Рувер-Авто",
    root_path="/api",
    lifespan=lifespan
)

app.include_router(products_router)
app.include_router(news_router)
app.include_router(content_router)
app.include_router(text_pages_router)
app.include_router(pages_router)
app.include_router(users_router)

admin = Admin(
    app,
    engine,
    authentication_backend=authentication_backend,
)
admin.add_view(MainContentAdmin)
admin.add_view(AboutUsAdmin)
admin.add_view(ProductsAdmin)
admin.add_view(ProductsInfoAdmin)
admin.add_view(ProductsImagesAdmin)
admin.add_view(PriceListAdmin)
admin.add_view(NewsAdmin)
admin.add_view(NewsImagesAdmin)
admin.add_view(TextPagesAdmin)
admin.add_view(UsersAdmin)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # При подключении Prometheus + Grafana подобный лог не требуется
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })
    return response
