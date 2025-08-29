from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

db_credentials = {
    'drivername': 'postgresql+psycopg2',  
    'host': "ec2-54-75-236-103.eu-west-1.compute.amazonaws.com",
    'username': "postgres.zgusezrdepdhjcleelrh",
    'password': "adriano@13",
    'database': "postgres",
    'port': 5432,
}

# Build the URL for the database connection
DATABASE_URL = URL.create(**db_credentials)

# Create the engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Example usage of the engine
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM employee"))  # wrapped in text()
    for row in result:
        print(row)
