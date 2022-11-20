# Python version: 3.9.6
# YouTube video: 09:16:14, 11/20/22
from . import models
from dotenv import load_dotenv
from .database import engine
from fastapi import FastAPI
import datetime
from .routers import post, user, auth, vote


load_dotenv()

# checks and create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World!!!!!!"}
