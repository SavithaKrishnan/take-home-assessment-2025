from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#change PSQL credentials as needed
DATABASE_URL = "postgresql://postgres:Choobertelephants2024@localhost:5432/state_registration_deadlines";

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()