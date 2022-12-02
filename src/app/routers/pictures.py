from models import *
from db import get_session
from helpers.image import write_image
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import File, UploadFile, Form

router = APIRouter(
    prefix="/pictures",
    tags=["pictures"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_categories(product_id: int = Form(...), file: UploadFile = File(...), 
                            session: AsyncSession = Depends(get_session)):
    """Создает новоое фото, сохраняет его на севрере и возвращает"""
    filepath = await write_image(file)
    picture = Pictures(product_id=product_id, link=filepath)
    session.add(picture)
    await session.commit()
    await session.refresh(picture)
    return picture