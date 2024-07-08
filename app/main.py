from app.products.router import router as products_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(products_router)
