from typing import Optional

from sqlalchemy.orm import Session

from src.db import Like


def set_like(
    db: Session,
    post_id: int,
    user_id: int,
    amount: int = 1
) -> Like:
    db_like = Like(
        post_id=post_id,
        user_id=user_id,
        amount=amount
    )
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like


def get_like(
    db: Session,
    post_id: int,
    user_id: int
) -> Optional[Like]:
    return db.query(Like).where(
        Like.user_id == user_id, Like.post_id == post_id
    ).first()
