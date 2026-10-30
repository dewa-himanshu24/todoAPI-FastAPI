import os
from dotenv import load_dotenv
from urllib.parse import quote
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


engine = create_engine(DATABASE_URL%quote(DATABASE_PASSWORD)) #Create a SQLAlchemy engine
# What is an sql alchemy engine?
# An Engine is a factory for connection objects. It encapsulates a connection pool that minimizes the cost of connection to the database by reusing existing connections and provides a consistent API for workng woth transcations.

Base = declarative_base()

metadata = MetaData() # Create a SQLAlchemy MetaData object

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Create a SQLAlchemy sessionmaker object

