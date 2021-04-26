import pandas as pd
import sqlalchemy

import Provider

db_user = Provider.conf.get("db.user")
db_pass = Provider.conf.get("db.pass")
engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{db_user}:{db_pass}@127.0.0.1:3306/ads")

con = engine.connect()


def get_all_table():
    df = pd.read_sql_query("""SELECT * FROM ads""", con)
    return df


def get_partial_table_by_range(start, end):
    statement = f"""SELECT * FROM ads WHERE `Index` BETWEEN '{start}' AND '{end}';"""
    df = pd.read_sql_query(statement, con)
    return df


def write_into_result(index, column_name, value):
    update = f"""UPDATE ads.RESULTS SET `{column_name}` = '{value}' WHERE  `Index` = {index};"""
    con.execute(update)
