from contextlib import asynccontextmanager
import time
from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.staticfiles import StaticFiles
from redis import asyncio as aioredis
from sqladmin import Admin

from app.database import engine
from app.admin.views import ProductsAdmin
from app.admin.views import ProductsInfoAdmin
from app.config import settings
from app.logger import logger
from app.products.router import router as products_router
from app.pages.router import router as pages_router
from app.load_images.router import router as images_router


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

app.include_router(pages_router)
app.include_router(images_router)

admin = Admin(app, engine)#, authentication_backend=authentication_backend)
admin.add_view(ProductsAdmin)
admin.add_view(ProductsInfoAdmin)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.middleware("https")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # При подключении Prometheus + Grafana подобный лог не требуется
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })
    return response
