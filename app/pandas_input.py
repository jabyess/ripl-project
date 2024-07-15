import sqlalchemy
import pandas as pd
from sqlalchemy import Integer, String, Numeric, Boolean
import config

db = config.Settings()

sql_connection_string = (
    f"postgresql://{db.DB_USER}:{db.DB_PASSWORD}@{db.DB_HOST}:{db.DB_PORT}/{db.DB_NAME}"
)

engine = sqlalchemy.create_engine(sql_connection_string)

bls_dtypes = {
    "ID": Integer,
    "AREA": Integer,
    "AREA_TITLE": String,
    "AREA_TYPE": Integer,
    "PRIM_STATE": String,
    "NAICS": Integer,
    "NAICS_TITLE": String,
    "I_GROUP": String,
    "OWN_CODE": Integer,
    "OCC_CODE": String,
    "OCC_TITLE": String,
    "O_GROUP": String,
    "TOT_EMP": Integer,
    "EMP_PRSE": Numeric,
    "JOBS_1000": Numeric,
    "LOC_QUOTIENT": Numeric,
    "PCT_TOTAL": Numeric,
    "PCT_RPT": Numeric,
    "H_MEAN": Numeric,
    "A_MEAN": Integer,
    "MEAN_PRSE": Numeric,
    "H_PCT10": Numeric,
    "H_PCT25": Numeric,
    "H_MEDIAN": Numeric,
    "H_PCT75": Numeric,
    "H_PCT90": Numeric,
    "A_PCT10": Integer,
    "A_PCT25": Integer,
    "A_MEDIAN": Integer,
    "A_PCT75": Integer,
    "A_PCT90": Integer,
    "ANNUAL": Boolean,
    "HOURLY": Boolean,
}

cols_to_keep = [
    "AREA_TITLE",
    "PRIM_STATE",
    "NAICS_TITLE",
    "OCC_TITLE",
    "O_GROUP",
    "TOT_EMP",
    "EMP_PRSE",
    "JOBS_1000",
    "LOC_QUOTIENT",
    "H_MEAN",
    "A_MEAN",
    "MEAN_PRSE",
    "H_PCT10",
    "H_PCT25",
    "H_MEDIAN",
    "H_PCT75",
    "H_PCT90",
    "A_PCT10",
    "A_PCT25",
    "A_MEDIAN",
    "A_PCT75",
    "A_PCT90",
]

df = pd.read_excel("./data/state_M2023_dl-ORIGINAL.xlsx", "state_M2023_dl")

mask_rule_1 = df == "*"
mask_rule_2 = df == "**"
mask_rule_3 = df == "#"

df = df.mask(mask_rule_1)
df = df.mask(mask_rule_2)
df = df.mask(mask_rule_3)

df = df.loc[:, cols_to_keep]

cleaned = df.ffill()


# test_df = pd.DataFrame([["VA", "test"], ["NY", "test"], ["MD", "test"]], columns=["state_name", "test"])
test_df = pd.DataFrame([["VA"], ["NY"], ["MD"]], columns=["state_name"])

# test_df = test_df.loc[:, "state_name"]

# print(test_df)


with engine.connect() as connection:
    cleaned.to_sql(
        "bls_data",
        index_label="id",
        con=connection,
        if_exists="replace",
        dtype=bls_dtypes,
    )

    test_df.to_sql("states", index_label="id", con=connection, if_exists="replace")
