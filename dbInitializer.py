import sqlalchemy
from sqlalchemy.sql import text

from utils import TextGenrator
import Provider

db_user = Provider.conf.get("db.user")
db_pass = Provider.conf.get("db.pass")
engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{db_user}:{db_pass}@127.0.0.1:3306")
with engine.connect() as con:
    statement = text("""CREATE DATABASE IF NOT EXISTS ads;""")
    con.execute(statement)
    statement = text("""DROP TABLE IF EXISTS ads.ads;""")
    con.execute(statement)
    statement = text("""CREATE TABLE ads.ads (
     `Index` INTEGER NOT NULL AUTO_INCREMENT,
     Id CHAR(5) NOT NULL,
     Name CHAR(15),
     PRIMARY KEY (`Index`));""")
    con.execute(statement)
    for x in range(Provider.conf.get("ads.total")):
        in_statement = f"""INSERT INTO ads.ads (Id,Name) VALUES ({x},'{TextGenrator.get_random_text()}')"""
        con.execute(in_statement)

    # statement = text("""DROP TABLE IF EXISTS ads.RESULTS;""")
    # con.execute(statement)
    # statement = text("""CREATE TABLE ads.RESULTS (
    #  `Index` INTEGER NOT NULL AUTO_INCREMENT,
    #  `Sorting-step1` CHAR(15),
    #  `Sorting-step2` CHAR(15),
    #  `Sorting-step3` CHAR(15),
    #  `Sorting-step1_Process_time` INTEGER,
    #  `Sorting-step2_Process_time` INTEGER,
    #  `Sorting-step3_Process_time` INTEGER,
    #  PRIMARY KEY (`Index`));""")
    # con.execute(statement)
    # for x in range(Provider.conf.get("ads.total")):
    #     in_statement = f"""INSERT INTO ads.RESULTS ()"""
    #     con.execute(in_statement)

