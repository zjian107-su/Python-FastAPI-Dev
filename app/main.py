# Python version: 3.9.6
# YouTube video: 11:11:21, 11/21/22
from . import models
from dotenv import load_dotenv
from .database import engine
from fastapi import FastAPI
import datetime
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from .page import html_content

load_dotenv()

# checks and create all tables
# Comment: comment the code below so ALEMBIC generates the table
# Comment: instead of sqlalchemy
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://www.google.com",
    "https://www.youtube.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    # test = "Daniel!!!"

    return HTMLResponse(content=html_content, status_code=200)
    # return {"Daniel"}
