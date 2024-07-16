from typing import Annotated
from fastapi import FastAPI, Depends
from functools import lru_cache
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import config, queries, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/states", response_model=list[schemas.StateSummary])
def states_summary(db: Session = Depends(get_db)):
    all_data = queries.get_state_summary(db)
    return all_data


@app.get("/api/state/{state_abbr}")
def state_detail(state_abbr: str, db: Session = Depends(get_db)):
    return queries.get_state_detail(state_abbr, db)
