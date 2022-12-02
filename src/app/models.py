from typing import Optional
from sqlmodel import Field, SQLModel
from typing import Optional

class Categories(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    photo: str

class Products(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str
    material : str
    price : float
    description : str
    rating : Optional[float] = 0
    category_id: int = Field(default=None, foreign_key="categories.id")

class Reviews(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    username : str
    content : str
    product_id: int = Field(default=None, foreign_key="products.id")
    rating: int 

class Pictures(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    link : str
    product_id: int = Field(default=None, foreign_key="products.id")




