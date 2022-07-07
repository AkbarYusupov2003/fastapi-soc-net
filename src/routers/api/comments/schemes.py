from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class CommentResponseScheme(BaseModel):
    id: int
    user_id: int
    post_id: int
    content: str
    created_at: datetime


class CreateCommentRequestScheme(BaseModel):
    post_id: int
    content: str


class UpdateCommentRequestScheme(BaseModel):
    id: int
    content: Optional[str] = None


class DeleteCommentRequestScheme(BaseModel):
    id: int
