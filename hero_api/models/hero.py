from typing import Optional

from sqlalchemy.orm import declarative_base
from sqlmodel import Field, SQLModel

class HeroBase(SQLModel):
    name: str
    secret_name: str
    weapon: Optional[str] = None
    headquarter: Optional[str] = None
    age: Optional[int] = None
