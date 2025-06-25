from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

DB_URL = "postgresql://postgres:Choobertelephants2024@localhost:5432/state_registration_deadlines"

connect_args = {"check_same_thread": False}
engine = create_engine(DB_URL, connect_args = connect_args)

print("engine created.")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        print(session)
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
print(SessionDep)

app = FastAPI()

class StateRegistrationInfo(SQLModel, table=True):
    state: str = Field(primary_key = True)
    deadline_in_person: str 
    deadline_by_mail: str
    deadline_online: str
    election_day_registration: str | None
    online_registration_link: str | None
    description: str | None
    '''   id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

    State: { type: DataTypes.STRING, primaryKey: true },
    DeadlineInPerson: DataTypes.STRING,
    DeadlineByMail: DataTypes.STRING,
    DeadlineOnline: DataTypes.STRING,
    ElectionDayRegistration: DataTypes.STRING,
    OnlineRegistrationLink: DataTypes.STRING,
    Description: DataTypes.STRING,'''

@app.get("/voter_registration_deadlines/")
async def read_voter_registration_deadlines(
    session: SessionDep # type: ignore
    ) -> list[StateRegistrationInfo]:
    print(session)
    statement = select(StateRegistrationInfo)
    #data = await self.session.execute(statement)
    data =  session.scalars(statement = statement).all()
    print(data)
    return data

read_voter_registration_deadlines( SessionDep )