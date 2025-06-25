from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated 
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import select


app = FastAPI()

class StateRegistrationInfo(BaseModel):
    State: str 
    Deadline_in_person: str 
    Deadline_by_mail: str
    Deadline_online: str
    Election_day_registration: str | None
    Online_registration_link: str | None
    Description: str | None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#db_dependency = Annotated(Session, Depends(get_db))
print("done with setup")

@app.get("/voter_reg_deadlines/")
def get_data():
    with Session(engine) as session:
        statement = select(models.StateRegistrationInfo)
        result = session.execute(statement).all()
        if not result:
            raise HTTPException(status_code=404, detail="No data in database. Make sure to load voter reg deadline data into database first.")
        print(result)
        return result
    
get_data()