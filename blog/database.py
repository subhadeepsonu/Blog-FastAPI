from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///./blog.db",connect_args={
    "check_same_thread":False
})

Sessionlocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)
Base = declarative_base()
