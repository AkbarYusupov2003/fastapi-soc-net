from fastapi import APIRouter

from .users.router import router as users_router
from .auth.router import router as auth_router
from .posts.router import router as posts_router
from .likes.router import router as likes_router
from .comments.router import router as comments_router

router = APIRouter(
    prefix='/api'
)
router.include_router(users_router)
router.include_router(auth_router)
router.include_router(posts_router)
router.include_router(likes_router)
router.include_router(comments_router)
