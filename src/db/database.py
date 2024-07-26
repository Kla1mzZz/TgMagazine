from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine('sqlite:///app/db/database.db')

session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass