from app import Base
from sqlalchemy import Column, string,BIGINT

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(string, nullable=False)
    email = Column(string(100), unique=True, nullable=False)
    admission_no = Column(BIGINT, nullable=False, unique=True)