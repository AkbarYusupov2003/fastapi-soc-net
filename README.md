# Simple Social Network powered by Python 3 and FastAPI

### Starting:
1. Install dependencies from `requirements.txt`
```shell
pip install -r requirements.txt
```
2. Create relation with the database
```shell
alembic init alembic
```
Next you need setup URI to the database in `alembic.ini` and set metadata in `alembic/env.py`\
Next make migrations:
```shell
alembic revision --autogenerate
```
And do a migrations:
```shell
alembic upgrade head
```
3. Setting up enviroment,
rename file `.env.simple` to `.env` and fill variables with values.
4. Start with uvicorn
```shell
uvicorn src.app:app --host 0.0.0.0 --port 8080
```

### Endpoints

##### Users
1. POST `/api/users/` - create user
2. PATCH `/api/users/` - update user

##### Authorization
1. POST `/api/auth/` - login
2. GET `/api/auth/` - confirm login

##### Posts
1. POST `/api/posts/` - create post
2. PATCH `/api/posts/` - update post
3. DELETE `/api/posts/` - delete post
4. GET `/api/posts/` - get post by id

##### Likes
1. POST `/api/likes/` - set like or dislike
2. GET `/api/likes/is_liked` - get is liked post
3. DELETE `/api/likes` - delete like or dislike

##### Comments
1. POST `/api/comments/` - create comment
2. PATCH `/api/comments/` - update comment
3. DELETE `/api/comments/` - delete comment
4. GET `/api/comments/` - get comment by id
5. GET `/api/comments/all` - get all comments of post
