from pydantic import BaseModel, HttpUrl
from typing import List

class NewCatData(BaseModel):
    url: HttpUrl
    score: int
    cat_group_id: int

class CatData(BaseModel):
    url: HttpUrl
    score: int

class CatGroup(BaseModel):
    cat_creation_prompt: str 
    cat_vission_prompt: str 
    cats: List[CatData]


class CatRatingResponse(BaseModel):
    groups: List[CatGroup]
