from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config

_db = config.Settings()

SQL_DB_URL = (
    f"postgresql://{_db.DB_USER}:{_db.DB_PASSWORD}@{_db.DB_HOST}:{_db.DB_PORT}/{_db.DB_NAME}"
)

engine = create_engine(SQL_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
