import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from .config import settings

# import time
# from fastapi.params import \
#     Body  # old fashion way to catch Postman POST params - Body
# from psycopg2.extras import RealDictCursor  # SQL table column
# import psycopg2

load_dotenv()

# LEGACY: old way to connect to DB with raw SQL execution. Now placed wit SQLACHEMY
# while True:
#     try:
#         # postgresql python code
#         # cursor_factory gives the return as a dictionary, with column name
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password=os.getenv('POSTGRESQL_PASSWORD'),
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB connection was successful!")
#         break
#     except Exception as error:
#         print("DB Connection fails")
#         print("Error:", error)
#         time.sleep(2)

# SQLALCHEMY DB CONNECTION
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"
# print(f'SQLALCHEMY_DATABASE_URL is {SQLALCHEMY_DATABASE_URL}', "from database.py")

print()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
