# Python version: 3.9.6
# YouTube video:
from random import randrange
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor  # SQL table column
from dotenv import load_dotenv
import os
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import \
    Body  # old fashion way to catch Postman POST params - Body


load_dotenv()
# checks and create table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()





while True:
    try:
        # postgresql python code
        # cursor_factory gives the return as a dictionary, with column name
        conn = psycopg2.connect(host='localhost', database='fastapi',
                                user='postgres', password=os.getenv('POSTGRESQL_PASSWORD'),
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("DB connection was successful!")
        break
    except Exception as error:
        print("DB Connection fails")
        print("Error:", error)
        time.sleep(2)


@app.get("/")
async def root():
    return {"message": "Hello World!!!!!!"}


@app.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
# def create_posts(user: dict = Body(...)): ## postman Body is the ..., with fastapi.params - Body
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # Previous version: memory database
    # return {"new post": f"My name is {user['name']} and My age is {user['age']}"}
    ## with fastapi.params - Body
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 1000000)
    # my_posts.append(post_dict)

    # Previous version02: postgresql database
    # !! Do NOT use f-string to avoid SQL injection attack
    # cursor.execute(
    #     "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit() 

    # print(**post.dict())
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"data": new_post}
    # return {"data": "pass"}


# TODO: from hardcode version --> DB version
# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts) - 1]
#     return {"detail": post}

@app.get("/posts/{id}")
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

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # delete post
    # find the index in the array that has required ID
    # my_posts.pop(index)

    # cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(
    #     "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return {"data": post_query.first()}
