from routers.categories import router as categories_router
from routers.products import router as products_router
from routers.pictures import router as pictures_router
from routers.reviews import router as reviews_router
from fastapi import FastAPI
from db import generate_db

app = FastAPI()

###закомментировать если не нужно генерировать бд
@app.on_event("startup")
async def on_startup():
    await generate_db()

app.include_router(categories_router)
app.include_router(products_router)
app.include_router(pictures_router)
app.include_router(reviews_router)
