from sqlalchemy.orm import Session, aliased
from sqlalchemy import func, and_
from .models import BLSData 
from .schemas import StateAbbr


def get_state_summary(db: Session):
    t1, t2 = aliased(BLSData), aliased(BLSData)
    highest_median_per_state = (
        db.query(t2.AREA_TITLE, func.max(t2.A_MEDIAN).label("max_median_wage"))
        .group_by(t2.AREA_TITLE)
        .subquery()
    )
    q = (
        db.query(t1.AREA_TITLE, t1.OCC_TITLE, t1.A_MEDIAN, t1.PRIM_STATE).join(
            highest_median_per_state,
            and_(
                t1.A_MEDIAN == highest_median_per_state.c.max_median_wage,
                t1.AREA_TITLE == highest_median_per_state.c.AREA_TITLE,
            ),
        )
    ).all()

    return q
    #### raw sql for comparison
    # sql = text(
    #     """
    #     select
    #     t1."AREA_TITLE",
    #     t1."OCC_TITLE",
    #     t1."A_MEDIAN",
    #     t1."PRIM_STATE"
    # from
    #     bls_data t1
    # join (
    #     select
    #         "AREA_TITLE",
    #         MAX("A_MEDIAN") as max_wage
    #     from
    #         bls_data
    #     group by
    #         "AREA_TITLE"
    # ) t2
    # on
    #     t1."AREA_TITLE" = t2."AREA_TITLE" and
    #     t1."A_MEDIAN" = t2.max_wage
    #     order by t1."AREA_TITLE";
    #     """
    # )


def get_state_detail(state_abbr, db: Session):
    return db.query(BLSData).filter(state_abbr.upper() == BLSData.PRIM_STATE, BLSData.OCC_TITLE == "All Occupations").all()

