from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    url=os.getenv("DATABASE_URL"),
    echo=True
    )   

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# we will inherit from this class to create each of the database models or classes
Base = declarative_base()