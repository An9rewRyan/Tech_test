from models import *
from db import get_session
from helpers.image import write_image
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import File, UploadFile, Form

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_categories(name: str = Form(...), file: UploadFile = File(...), 
                            session: AsyncSession = Depends(get_session)):
    """Создает новую категорию товаров и возвращает ее"""
    filepath = await write_image(file)
    category= Categories(name=name, photo=filepath)
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category

