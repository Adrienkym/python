#File for connecting to  our db
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base,sessionmaker


db_credentials = {
    'drivername': 'postgresql+psycopg2',  
    'host': "ec2-54-75-236-103.eu-west-1.compute.amazonaws.com",
    'username': "postgres.zgusezrdepdhjcleelrh",
    'password': "adriano@13",
    'database': "postgres",
    'port': 5432,
}

#BUILD URL
DATABASE_URL=URL.create(**db_credentials)

engine=create_engine(DATABASE_URL,echo=True,future=True)


SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

#BASE
Base=declarative_base()