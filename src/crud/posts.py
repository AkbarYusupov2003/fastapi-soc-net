from typing import Optional

from sqlalchemy.orm import Session

from src.db import Post


def create_post(
    db: Session,
    owner_id: int,
    content: str
) -> Post:
    db_post = Post(
        content=content,
        owner_id=owner_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(
    db: Session,
    post_id: int
) -> Optional[Post]:
    return db.query(Post).where(Post.id == post_id).first()


def update_post(
    db: Session,
    db_post: Post
) -> Post:
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(
    db: Session,
    db_post: Post
) -> None:
    db.delete(db_post)
    db.commit()
