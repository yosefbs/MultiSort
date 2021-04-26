import sqlalchemy

import Provider
from utils.FileHandler import FileHandler


db_user = Provider.conf.get("db.user")
db_pass = Provider.conf.get("db.pass")
engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{db_user}:{db_pass}@127.0.0.1:3306/ads")


def write_result_to_db():
    files = []
    with open('Sorting-step1.txt', 'r') as res1, open('Sorting-step2.txt', 'r') as res2, open('Sorting-step3.txt', 'r') as res3:
        total_lines = Provider.conf.get("ads.total")
        iter1 = iter(res1.readline, '')
        iter2 = iter(res2.readline, '')
        iter3 = iter(res3.readline, '')
        with engine.connect() as con:
            for i in range(0,total_lines,1):
                update = f"""UPDATE ads.RESULTS SET `Sorting-step1`='{next(iter1)}', `Sorting-step2`='{next(iter2)}',`Sorting-step3`='{next(iter3)}' WHERE `Index` = {i+1};"""
                con.execute(update)
                if i%100 == 0:
                    print(f"complete {(i / total_lines)*100}%")


write_result_to_db()
print("complete 100%")
