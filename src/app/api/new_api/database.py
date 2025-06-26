from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#change PSQL credentials as needed
DATABASE_URL = "postgresql://postgres:test@localhost:5432/state_registration_deadlines";

engine = create_engine(DATABASE_URL)

Base = declarative_base()