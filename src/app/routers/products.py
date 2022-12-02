from models import Products, Pictures, Reviews
from db import get_session
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from schema import Products_ext, Products_short

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_products(product: Products, session: AsyncSession = Depends(get_session)):
    """Создает новый товар и возвращает его"""
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product

@router.get("/get/{id}")
async def get_product(id: int, extended: bool | None = False, session: AsyncSession = Depends(get_session)):
    """Возвращает развернутую карточку товара (фото + отзывы)"""
    statement = select(Products).where(Products.id == id)
    result = await session.execute(statement)
    product = result.scalars().first()

    if extended == True:
        query_result_pics = await session.execute(select(Pictures).where(Pictures.product_id == id))
        pictures = list(query_result_pics.scalars().all())
        query_result_revs = await session.execute(select(Reviews).where(Reviews.product_id == id))
        reviews = list(query_result_revs.scalars().all())
        session.commit()

        product_out = Products_ext(**product.dict())
        pictures = ["http://localhost:8000"+picture.link for picture in pictures]
        product_out.pictures = pictures
        product_out.reviews = reviews
    else:
        product_out = Products(**product.dict())

    return product_out

@router.get("/get")
async def get_products(limit: int|None = 20, category: int | None = None, order_by: str|None = 'id', session: AsyncSession = Depends(get_session)):
    """Возвращает список продуктов в укороченном формате. Поддерживается параметризация."""
    statement = select(Products)
    all_products = []
    if category:
        statement = statement.where(Products.category_id == category)
    statement=statement.order_by(order_by).limit(limit)
    query_result_prods = await session.execute(statement)
    products = query_result_prods.scalars().all()
    for product in products:
        res_pic = await session.execute(select(Pictures).where(Pictures.product_id == product.id).limit(1))
        pic = res_pic.scalars().one_or_none()
        if pic != None:
            pic_link = "http://localhost:8000"+pic.link
        else:
            pic_link = "Нет картинок"
        short_prod = Products_short(id=product.id, name=product.name, price=product.price, picture=pic_link)
        all_products.append(short_prod)
    
    await session.commit()

    return all_products



    





