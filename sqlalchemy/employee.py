from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import Text
from engine import engine  

# Base class
class Base(DeclarativeBase):
    pass

# Employee model
class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False, unique=True)

# Create the table
Base.metadata.create_all(engine)

# Example usage
with Session(engine) as session:
    new_employee = Employee(name="John Doe", email="doe@doe.com")
    session.add(new_employee)
    session.commit()
