from models import *
from db import get_session
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from helpers.rating import count_rate

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_reviews(review: Reviews, session: AsyncSession = Depends(get_session)):
    """Создает новый обзор, обновляет рейтинг товара возвращает обзор"""
    session.add(review)
    prod_query = await session.execute(select(Products).where(Products.id == review.product_id))
    product = prod_query.scalars().first()

    rev_query = await session.execute(select(Reviews).where(Reviews.product_id==review.product_id))
    reviews = rev_query.scalars().all()
    product.rating = count_rate(reviews)
    session.add(product)
    await session.commit()

    return review