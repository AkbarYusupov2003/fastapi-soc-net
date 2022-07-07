from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from src.routers.api.posts.schemes import OkResponseScheme
from src.crud import likes, tokens, posts
from src.db import get_db
from .schemes import (
    LikeResponseScheme,
    LikeRequestScheme,
    DeleteLikeRequestScheme
)

router = APIRouter(
    prefix='/likes',
    tags=['likes']
)


@router.post('/', response_model=LikeResponseScheme)
async def set_like_or_dislike_to_post(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: LikeRequestScheme
):
    """Set like or dislike to post;
    if amount more 0 or amount equal 0 then it like else it dislike"""

    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, data.post_id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    db_like = likes.get_like(db, db_post.id, db_user.id)
    data.amount = -1 if data.amount < 0 else 1
    if db_like:
        db_like.amount = data.amount
        db_like = likes.update_like(db, db_like)
    else:
        db_like = likes.set_like(
            user_id=db_user.id,
            post_id=db_post.id,
            amount=data.amount
        )
    return db_like


@router.get('/is_liked', response_model=LikeResponseScheme)
async def post_is_liked(
    db: Session = Depends(get_db),
    token: str = Query(None),
    post_id: int = Query(None)
):
    """Get is post liked"""

    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, post_id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    db_like = likes.get_like(db, db_user.id, db_post.id)
    return db_like


@router.delete('/', response_model=OkResponseScheme)
async def delete_like_or_dislike(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: DeleteLikeRequestScheme
):
    """Delete like or dislike"""

    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, data.post_id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    db_like = likes.get_like(db, db_post.id, db_user.id)
    if not db_like:
        raise HTTPException(404, 'You didn\'t like or dislike')
    likes.delete(db, db_like)
    return {'ok': True}
