# Python version: 3.9.6
# YouTube video:
import psycopg2
from . import models
from psycopg2.extras import RealDictCursor  # SQL table column
from dotenv import load_dotenv
import os
import time
from .database import engine
from fastapi import FastAPI
from fastapi.params import \
    Body  # old fashion way to catch Postman POST params - Body
import datetime
from .routers import post, user, auth

print(datetime.datetime.now(tz=None))
load_dotenv()

# checks and create all tables
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

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World!!!!!!"}