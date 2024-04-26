from pydantic import BaseModel, HttpUrl
from typing import List

class NewCatData(BaseModel):
    url: HttpUrl
    score: int
    cat_group_id: int
    
class ImageData(BaseModel):
    url: HttpUrl
    score: int

class ImageGroup(BaseModel):
    images: List[ImageData]

class CatRatingResponse(BaseModel):
    groups: List[ImageGroup]
