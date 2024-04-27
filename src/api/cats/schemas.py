from pydantic import BaseModel, HttpUrl
from typing import List

class NewCatData(BaseModel):
    url: str
    score: int
    cat_group_id: int

class CatData(BaseModel):
    url: str
    score: int

class CatGroup(BaseModel):
    cat_creation_prompt: str 
    cat_vision_prompt: str 
    cats: List[CatData]


class CatRatingResponse(BaseModel):
    groups: List[CatGroup]
