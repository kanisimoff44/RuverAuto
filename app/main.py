from fastapi import FastAPI

from app.products.router import router as products_router
from app.pages.router import router as pages_router

app = FastAPI()
app.include_router(products_router)

app.include_router(pages_router)
