# Python version: 3.9.6
# YouTube video:

from random import randrange
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor # SQL table column
from dotenv import load_dotenv
import os
import time
load_dotenv()


from fastapi import FastAPI, Response, status, HTTPException  # api dev library
from fastapi.params import \
    Body  # old fashion way to catch Postman POST params - Body
from pydantic import BaseModel  # restrict input type and format returns

app = FastAPI()
my_posts = [{"title": "Daniel and Robyn", "content": "Daniel and Robyn visit NYC", "rating": "27", "id": 2}, {"title": "Nabi", "content": "Nabi is the best dog", "id": 3}
     ]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index


# name str, age int
class Blog(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:
    try:
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
async def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {"data": posts}

@app.post("/createposts", status_code=status.HTTP_201_CREATED)
# def create_posts(user: dict = Body(...)): ## postman Body is the ..., with fastapi.params - Body
def create_posts(post: Blog):
    # Previous version: memory database
    # return {"new post": f"My name is {user['name']} and My age is {user['age']}"}
    ## with fastapi.params - Body
    # post_dict = blog.dict()
    # post_dict['id'] = randrange(0, 1000000)
    # my_posts.append(post_dict)


    # Current version: postgresql database
    # !! Do NOT use f-string to avoid SQL injection attack
    cursor.execute(
        "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))

    new_post = cursor.fetchone()

    conn.commit() 
    return {"data": new_post}

# TODO: from hardcode version --> DB version
# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts) - 1]
#     return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id: {id} was not found')
        # hardcode to deal with exception
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
        
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # delete post
    # find the index in the array that has required ID
    # my_posts.pop(index)

    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Blog):

    cursor.execute(
        "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    return {"message": updated_post}
