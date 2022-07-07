import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True)
    first_name = sa.Column(sa.String(50))
    last_name = sa.Column(sa.String(50), nullable=True)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    last_login_at = sa.Column(sa.DateTime, nullable=True)

    posts = relationship('Post')


class Token(Base):
    __tablename__ = 'tokens'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    type_ = sa.Column(sa.String(25))
    token = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime, default=sa.func.now())


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    content = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, default=sa.func.now(), onupdate=sa.func.now())

    comments = relationship('Comment')
    likes = relationship('Like')


class Like(Base):
    __tablename__ = 'likes'

    id = sa.Column(sa.Integer, primary_key=True)
    post_id = sa.Column(sa.Integer, sa.ForeignKey('posts.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    amount = sa.Column(sa.Integer, default=1)


class Comment(Base):
    __tablename__ = 'comments'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    post_id = sa.Column(sa.Integer, sa.ForeignKey('posts.id'))
    content = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
