from sqlalchemy import Column, String
from database import Base

class StateRegistrationInfo(Base):
    __tablename__ = "voter_registration_deadlines"

    State = Column(String, primary_key=True, index=True) 
    DeadlineInPerson = Column(String) 
    DeadlineByMail = Column(String)
    DeadlineOnline = Column(String)
    ElectionDayRegistration = Column(String, None)
    OnlineRegistrationLink = Column(String, None)
    Description = Column(String, None)