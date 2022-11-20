# Python version: 3.9.6
# YouTube video:
from . import models
from dotenv import load_dotenv
from .database import engine
from fastapi import FastAPI
import datetime
from .routers import post, user, auth


load_dotenv()

# checks and create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World!!!!!!"}