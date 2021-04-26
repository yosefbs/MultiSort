import pandas as pd
import sqlalchemy

import Provider

db_user = Provider.conf.get("db.user")
db_pass = Provider.conf.get("db.pass")
engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{db_user}:{db_pass}@127.0.0.1:3306/ads")


def get_all_table():
    with engine.connect() as con:
        df = pd.read_sql_query("""SELECT * FROM ads""", con)
    return df


def get_partial_table_by_range(start, end):
    statement = f"""SELECT * FROM ads WHERE `Index` BETWEEN '{start}' AND '{end}';"""
    df = None
    with engine.connect() as con:
        df = pd.read_sql_query(statement, con)
    return df

def write_column(data,column_name):
    print(data)

