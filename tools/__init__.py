import pandas as pd

def define_cohort(df: pd.DataFrame, law_col: str, time_col: str = 'year', unit_col: str = 'state_abb') -> pd.DataFrame:
    """Define cohort year for each unit based on the first year the law was treated."""

    df = df.copy()
    treated = df[df[law_col]==1]

    cohorts = treated.groupby(unit_col).min().reset_index()
    df['cohort_year'] = df[unit_col].map(cohorts.set_index(unit_col)[time_col])

    return df



