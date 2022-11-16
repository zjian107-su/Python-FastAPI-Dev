# Python version: 3.9.6
# YouTube video:

from random import randrange
from typing import Optional

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


@app.get("/")
async def root():
    return {"message": "Hello World!!!!!!"}


@app.get("/posts")
async def get_posts():
    return my_posts

@app.post("/createposts", status_code=status.HTTP_201_CREATED)
# def create_posts(user: dict = Body(...)): ## postman Body is the ..., with fastapi.params - Body
def create_posts(blog: Blog):
    # return {"new post": f"My name is {user['name']} and My age is {user['age']}"}
    ## with fastapi.params - Body
    post_dict = blog.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
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

    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Blog):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')
    post_dict = post.dict()
    print(f'post_dict is {post_dict}')
    post_dict['id'] = id
    my_posts[index] = post_dict
    print(f'my_posts[index] is {my_posts[index]}')
    return {"message": "updated post"}
