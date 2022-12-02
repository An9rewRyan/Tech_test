from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional, List

class Reviews_out(BaseModel):
    """Вспомогательный класс обзора, который нужен для корректного вывода связанных с продуктом обзоров"""
    id : int
    username : str
    content : str
    product_id: int
    rating: int 

class Products_ext(BaseModel):
    """Вспомогательный класс продукта, который нужен для корректного вывода связанных объектов"""
    id: int
    name : str
    material : str
    price : float
    description : str
    rating : Optional[float] = 0
    category_id: int
    reviews: List[Reviews_out] = []
    pictures: List[str] = []

class Products_short(BaseModel):
    """Укороченная модель продукта для вывода всех продуктов"""
    id: int
    name: str
    picture: str
    price: float


