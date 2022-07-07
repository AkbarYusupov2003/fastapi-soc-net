from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class PostResponseScheme(BaseModel):
    id: int
    owner_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class OkResponseScheme(BaseModel):
    ok: bool


class CreatePostRequestScheme(BaseModel):
    content: str


class UpdatePostRequestScheme(BaseModel):
    id: int
    content: Optional[str] = None


class DeletePostRequestScheme(BaseModel):
    id: int
