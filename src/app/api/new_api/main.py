from fastapi import FastAPI, HTTPException
import models 
from database import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

app = FastAPI()

@app.get("/voter_reg_deadlines/")
def get_data():
    with Session(engine) as session:
        statement = select(models.StateRegistrationInfo.State, models.StateRegistrationInfo.DeadlineInPerson, models.StateRegistrationInfo.DeadlineByMail, models.StateRegistrationInfo.DeadlineOnline, models.StateRegistrationInfo.ElectionDayRegistration, models.StateRegistrationInfo.OnlineRegistrationLink, models.StateRegistrationInfo.Description)
        result = session.execute(statement).all()
        if not result:
            raise HTTPException(status_code=404, detail="No data in database. Make sure to load voter reg deadline data into database first.")

        columns = ['State', 'Deadline_in_person', 'Deadline_by_mail', 'Deadline_online', 'Election_day_registration', 'Online_registration_link', 'Description']

        result_json = []
        for r in result:
            r_dict = {}
            for idx, l in enumerate(columns):
                r_dict[l] = r[idx]
            result_json.append(r_dict)
        return result_json
    
get_data()