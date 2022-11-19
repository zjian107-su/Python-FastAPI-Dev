from .. import models, schemas
from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import Response, status, HTTPException, Depends
from .. import oauth2

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(user: dict = Body(...)): ## postman Body is the ..., with fastapi.params - Body
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 user_id: int = Depends(oauth2.get_current_user)):
    # Previous version02: postgresql database
    # !! Do NOT use f-string to avoid SQL injection attack
    # cursor.execute(
    #     "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
    #     (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    print(f'User {user_id} has made the post request')  # check if the login is successful by return
    # requested
    # user id

    # print(**post.dict())
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
    # return {"data": "pass"}


# TODO: from hardcode version --> DB version
# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts) - 1]
#     return {"detail": post}

@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} was not found')
        # hardcode to deal with exception
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # delete post
    # find the index in the array that has required ID
    # my_posts.pop(index)

    # cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    print(f'User with {user_id} has made the delete request')  # check if the login is successful by return
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
    #     (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    print(f'User with {user_id} has made the update request')  # check if the login is successful by return

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()
