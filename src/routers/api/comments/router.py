from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from src.crud import comments, tokens, posts
from src.db import get_db
from .schemes import (
    CommentResponseScheme,
    CreateCommentRequestScheme,
    UpdateCommentRequestScheme,
    DeleteCommentRequestScheme,
)
from src.routers.api.posts.schemes import OkResponseScheme

router = APIRouter(
    prefix='/comments',
    tags=['comments']
)


@router.post('/', response_model=CommentResponseScheme)
async def create_comment(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: CreateCommentRequestScheme
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_post = posts.get_post(db, data.post_id)
    if not db_post:
        raise HTTPException(404, 'Post not found')
    db_comment = comments.create_comment(
        db, db_post.id, db_user.id, content=data.content
    )
    return db_comment


@router.patch('/', response_model=CommentResponseScheme)
async def update_comment(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: UpdateCommentRequestScheme
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_comment = comments.get_comment(db, data.id)
    if data.content:
        db_comment.content = data.content
    db_comment = comments.update_comment(db, db_comment)
    return db_comment


@router.get('/', response_model=CommentResponseScheme)
async def get_comment(
    db: Session = Depends(get_db),
    token: str = Query(None),
    comment_id: int = Query(None)
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_comment = comments.get_comment(db, comment_id)
    if not db_comment:
        raise HTTPException(404, 'Comment not found')
    return db_comment


@router.get('/all', response_model=List[CommentResponseScheme])
async def get_all_comments(
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
    db_comments = comments.get_comments(db, post_id)
    return db_comments


@router.delete('/', response_model=OkResponseScheme)
async def delete_comment(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: DeleteCommentRequestScheme
):
    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_comment = comments.get_comment(db, data.id)
    if not db_comment:
        raise HTTPException(404, 'Comment not found')
    comments.delete(db, db_comment)
    return {'ok': True}
