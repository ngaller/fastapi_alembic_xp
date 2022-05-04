from typing import Optional

from sqlmodel import Field
from hero_api.models.hero import HeroBase


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
