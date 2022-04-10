import imp
from pydantic import BaseModel
from typing import List

class Img(BaseModel):
    url: str

class Slider(BaseModel):
    imgs: List[Img]