import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_GP_URL")

engine = sqlalchemy.create_engine(database_url)
connection = engine.connect()