from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from src.crud import tokens, posts
from src.db import get_db
from .schemes import (
    OkResponseScheme,
    PostResponseScheme,
    CreatePostRequestScheme,
    UpdatePostRequestScheme,
    DeletePostRequestScheme
)

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.post('/', response_model=PostResponseScheme)
async def create_post(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: CreatePostRequestScheme
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.create_post(db, db_user.id, data.content)
    return db_post


@router.get('/', response_model=PostResponseScheme)
async def get_by_id(
    db: Session = Depends(get_db),
    token: str = Query(None),
    post_id: int = Query(None)
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, post_id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    return db_post


@router.patch('/', response_model=PostResponseScheme)
async def update_post(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: UpdatePostRequestScheme
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, data.id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    if db_post.owner_id != db_user.id:
        raise HTTPException(403, 'You are not owner of this post')
    if data.content:
        db_post.content = data.content
    db_post = posts.update_post(db, db_post)
    return db_post


@router.delete('/', response_model=OkResponseScheme)
async def delete_post(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: DeletePostRequestScheme
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, data.id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    if db_post.owner_id != db_user.id:
        raise HTTPException(403, 'You are not owner of this post')
    posts.delete_post(db, db_post)
    return {'ok': True}
