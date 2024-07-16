from sqlalchemy import Integer, String, Float, Column, inspect
from .database import Base


class BLSData(Base):
    __tablename__ = "bls_data"

    id = Column(Integer, primary_key=True)

    AREA_TITLE = Column(String)
    PRIM_STATE = Column(String)
    NAICS_TITLE = Column(String)
    OCC_TITLE = Column(String)
    O_GROUP = Column(String)
    TOT_EMP = Column(Integer)
    EMP_PRSE = Column(Float)
    JOBS_1000 = Column(Float)
    LOC_QUOTIENT = Column(Float)
    H_MEAN = Column(Float)
    A_MEAN = Column(Integer)
    MEAN_PRSE = Column(Float)
    H_PCT10 = Column(Float)
    H_PCT25 = Column(Float)
    H_MEDIAN = Column(Float)
    H_PCT75 = Column(Float)
    H_PCT90 = Column(Float)
    A_PCT10 = Column(Integer)
    A_PCT25 = Column(Integer)
    A_MEDIAN = Column(Integer)
    A_PCT75 = Column(Integer)
    A_PCT90 = Column(Integer)

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}


# class State(Base):
#     __tablename__ = "states"

#     id = Column(Integer, primary_key=True)
#     AREA_TITLE = Column(String)
#     PRIM_STATE = Column(String)
#     OCC_CODE = Column(Integer)
#     OCC_TITLE = Column(String)
#     TOT_EMP = Column(Integer)
#     EMP_PRSE = Column(Float)
#     JOBS_1000 = Column(Float)
#     LOC_QUOTIENT = Column(Float)
#     H_MEAN = Column(Float)
#     A_MEAN = Column(Integer)
#     MEAN_PRSE = Column(Float)
#     H_PCT10 = Column(Float)
#     H_PCT25 = Column(Float)
#     H_MEDIAN = Column(Float)
#     H_PCT75 = Column(Float)
#     H_PCT90 = Column(Float)
#     A_PCT10 = Column(Integer)
#     A_PCT25 = Column(Integer)
#     A_MEDIAN = Column(Integer)
#     A_PCT75 = Column(Integer)
#     A_PCT90 = Column(Integer)
