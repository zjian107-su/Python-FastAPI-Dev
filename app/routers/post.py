from .. import models, schemas
from typing import List, Optional
from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import Response, status, HTTPException, Depends
from .. import oauth2

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


# GET ALL permitted posts
@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user),
                    limit: int = 100,
                    skip: int = 0,
                    search: Optional[str] = ""
                    ):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    # posts_query_sql = db.query(models.Post).filter(models.Post.owner_id == current_user.id).limit(limit)
    posts_query_sql = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip)
    posts = posts_query_sql.all()

    print(posts_query_sql)
    return posts


# POST one post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(user: dict = Body(...)): ## postman Body is the ..., with fastapi.params - Body
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    # Previous version02: postgresql database
    # !! Do NOT use f-string to avoid SQL injection attack
    # cursor.execute(
    #     "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
    #     (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    print(f'User {current_user} has made the post request')  # check if the login is successful by return

    # print(**post.dict())
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
    # return {"data": "pass"}


# GET one post
@router.get("/{id}")
def get_post(id: int,
             db: Session = Depends(get_db),
             current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} was not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform load")

    return post


# DELETE post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    print(f'User with {current_user} has made the delete request')  # check if the login is successful by return
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform delete")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# UPDATE post
@router.put("/{id}")
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
    #     (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    print(f'User with {current_user} has made the update request')  # check if the login is successful by return

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform update")

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()
