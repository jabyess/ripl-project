from typing import Annotated
from fastapi import FastAPI, Depends, Response
from fastapi.encoders import jsonable_encoder
from functools import lru_cache
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import config, queries, models, schemas
import json

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
    # results = all_data.serialize()

    return all_data


@app.get("/api/state/{state}")
def state_detail(state: str, db: Session = Depends(get_db)):
    # return [{"state": state}]
    return queries.get_state_detail(state, db)


# test route to make sure my settings object worked
@app.get("/api/settings")
def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {"db_name": settings.DB_NAME, "db_host": settings.DB_HOST}
