import os
from dotenv import load_dotenv
from sqlmodel import SQLModel
from pathlib import Path
from models import *
from random import randint
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent
load_dotenv(os.path.join(BASE_DIR, ".env"))
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def init_db():
    """"Фукнция для генерации исходных таблиц"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    """Вовзращает генератор асинхронной сессии"""
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def generate_db():
    """Одноразовая функция для генерации исходной бд"""
    chairs = Categories(name="Стулья", photo="http://localhost:8000/files/Стул.jpeg")
    sofas = Categories(name="Диваны", photo="http://localhost:8000/files/Диван.jpeg")
    reviews = []
    pictures = []
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [chairs, sofas
            ])
        for i in range(1, 41):
            indx = i
            if i < 21:
                name = "Стул"
                material = "Дуб"
                category = 1
            else:
                name = "Диван"
                material = "Бычья кожа"
                category = 2
                indx-=20

            product = Products(name=f'{name}#{indx}', material=material, price=randint(100, 1000), 
                            description=f'Просто отличный {name}!', rating = 0, category_id=category)
            session.add(
                product
            )
            await session.commit()
            await session.refresh(product)
            mid_rate = 0
            for i in range(1, 4):
                picture = Pictures(link=f'/files/{name}.jpeg', product_id=product.id)
                review = Reviews(username="Michael Jordan", content=f'О боже! Вот это {name}! Всем рекомендую!', product_id=product.id, rating=randint(1, 5))
                pictures.append(picture)
                reviews.append(review)
                mid_rate += review.rating
            product.rating = round(mid_rate/3, 2)
            session.add(
                product
            )
            await session.commit()
        for pic in pictures:
            session.add(pic)
        for rev in reviews:
            session.add(rev)
        await session.commit()
