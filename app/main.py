import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from app.database import engine
from app.admin.views import ProductsAdmin
from app.logger import logger
from app.products.router import router as products_router
from app.pages.router import router as pages_router

app = FastAPI(
    title="Рувер-Авто",
    root_path="/api"
)

app.include_router(products_router)

app.include_router(pages_router)

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

admin = Admin(app, engine)#, authentication_backend=authentication_backend)
admin.add_view(ProductsAdmin)
