from typing import Optional, List

from sqlalchemy.orm import Session

from src.db import Comment


def create_comment(
    db: Session,
    post_id: int,
    user_id: int,
    content: str
) -> Comment:
    db_comment = Comment(
        post_id=post_id,
        user_id=user_id,
        content=content
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_comment(
    db: Session,
    db_comment: Comment,
) -> Comment:
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments(
    db: Session,
    post_id: int
) -> List[Comment]:
    return db.query(Comment).where(Comment.post_id == post_id).all()


def get_comment(
    db: Session,
    comment_id: int
) -> Optional[Comment]:
    return db.query(Comment).where(Comment.id == comment_id).first()


def delete_comment(
    db: Session,
    db_comment: Comment
) -> None:
    db.delete(db_comment)
    db.commit()
