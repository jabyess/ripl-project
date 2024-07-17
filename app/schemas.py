from pydantic import BaseModel, Field

class AllDataBase(BaseModel):
    id: int
    AREA: int
    AREA_TITLE: str
    AREA_TYPE: int
    PRIM_STATE: str
    NAICS: int
    NAICS_TITLE: str
    I_GROUP: str
    OWN_CODE: int
    OCC_CODE: str
    OCC_TITLE: str
    O_GROUP: str
    TOT_EMP: int
    EMP_PRSE: float
    JOBS_1000: float
    LOC_QUOTIENT: float
    PCT_TOTAL: float
    PCT_RPT: float
    H_MEAN: float
    A_MEAN: int
    MEAN_PRSE: float
    H_PCT10: float
    H_PCT25: float
    H_MEDIAN: float
    H_PCT75: float
    H_PCT90: float
    A_PCT10: int
    A_PCT25: int
    A_MEDIAN: int
    A_PCT75: int
    A_PCT90: int
    ANNUAL: bool
    HOURLY: bool

    class Config:
        from_attributes = True 


class StateSummary(BaseModel):
    AREA_TITLE: str
    A_MEDIAN: float
    OCC_TITLE: str
    PRIM_STATE: str


class StateAbbr(BaseModel):
    state_abbr: str = Field(max_length=2, min_length=2, examples=["NY"])

class StateDetail(BaseModel):
    AREA_TITLE: str
    PRIM_STATE: str
    OCC_TITLE: str
    TOT_EMP: int
    EMP_PRSE: float
    JOBS_1000: float
    LOC_QUOTIENT: float
    H_MEAN: float
    A_MEAN: int
    MEAN_PRSE: float
    H_PCT10: float
    H_PCT25: float
    H_MEDIAN: float
    H_PCT75: float
    H_PCT90: float
    A_PCT10: int
    A_PCT25: int
    A_MEDIAN: int
    A_PCT75: int
    A_PCT90: int