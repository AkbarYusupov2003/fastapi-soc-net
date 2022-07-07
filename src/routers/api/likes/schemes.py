from pydantic import BaseModel


class LikeResponseScheme(BaseModel):
    post_id: int
    user_id: int


class LikeRequestScheme(BaseModel):
    post_id: int
    amount: int


class DeleteLikeRequestScheme(BaseModel):
    post_id: int
