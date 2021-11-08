from datetime import datetime, timedelta
from logging import getLogger
from src.DB.DB_Adapter import DBAdapter
import matplotlib.pyplot as plt

logger = getLogger(__name__)
# 데이터를 가져올 서버의 정보
database = {
    "database": 'ppc',
    "user": 'user',
    "password": '1234',
    "host": "13.125.210.112",
    "port": 12100,
}
db = DBAdapter(name="database", direct=database)


print("hello owo")
table = "app_collect_generation"
select_sql = f"SELECT COLUMN_NAME, DATA_TYPE " \
             f"FROM INFORMATION_SCHEMA.COLUMNS " \
             f"WHERE TABLE_CATALOG = 'ppc' " \
             f"AND TABLE_NAME = '{table}' " \
             f"ORDER BY ORDINAL_POSITION;"
column_list_raw = db.fetch_data_by_sql(select_sql)
column_list = []
column_type = []
for token in column_list_raw:
    column_list.append(token[0])
    column_type.append(token[1])
del column_list[0]
del column_type[0]
column_list_str = str(column_list).replace("[", "").replace("]", "").replace("'", "")
select_sql = f"SELECT {column_list_str} FROM {table}"
data_all = db.fetch_data_by_sql(select_sql)


def data_dupe_detector(db, table, data_list, column_str, column_type):
    column = column_str.split(", ")
    i = 0
    column_dict = {}
    select_sql = f"SELECT {column_str} FROM {table}"
    data_list = db.fetch_data_by_sql(select_sql)
    compare_column = ['target', 'site_id']
    compare_column_str = "target, site_id"
    for data in data_list:
        select_sql = f"SELECT COUNT(*) FROM {table} WHERE "
        delete_sql = f"DELETE FROM {table} WHERE "
        insert_sql = f"INSERT INTO {table}({column_str}) VALUES ("
        types = 0
        i = 0
        while i < len(data):
            if column[i] in compare_column and type(data[i]) == datetime:
                types = 1
            elif column[i] in compare_column and type(data[i]) != datetime:
                types = 2
            elif column[i] not in compare_column and type(data[i]) == datetime:
                types = 3
            elif column[i] not in compare_column and type(data[i]) != datetime:
                types = 4
            if types == 1:
                select_sql = select_sql + f"AND {column[i]} = (TO_TIMESTAMP('{data[i]}', 'yyyy-mm-dd HH24:MI:SS.ffffff')) "
                delete_sql = delete_sql + f"AND {column[i]} = (TO_TIMESTAMP('{data[i]}', 'yyyy-mm-dd HH24:MI:SS.ffffff')) "
                insert_sql = insert_sql + f"(TO_TIMESTAMP('{data[i]}', 'yyyy-mm-dd HH24:MI:SS.ffffff')), "
            elif types == 2:
                select_sql = select_sql + f"AND {column[i]} = {data[i]} "
                delete_sql = delete_sql + f"AND {column[i]} = {data[i]} "
                insert_sql = insert_sql + f"{data[i]}, "
            elif types == 3:
                insert_sql = insert_sql + f"(TO_TIMESTAMP('{data[i]}', 'yyyy-mm-dd HH24:MI:SS.ffffff')), "
            elif types == 4:
                insert_sql = insert_sql + f"{data[i]}, "
            i = i + 1
        select_sql = select_sql.replace("WHERE AND", "WHERE")
        select_sql = select_sql.rstrip(', ')
        select_sql = select_sql + ";"
        delete_sql = delete_sql.replace("WHERE AND", "WHERE")
        delete_sql = delete_sql.rstrip(', ')
        delete_sql = delete_sql + ";"
        insert_sql = insert_sql.rstrip(', ')
        insert_sql = insert_sql + ");"
        dupe_checker = db.fetch_data_by_sql(select_sql)
        token = True
        if dupe_checker[0][0] <= 1:
            print(f"not duplicated. data : {data}")
            token = True
        else:
            print(f"duplicated. data : {data}")
            token = False
        if token:
            print("search for next one")
        else:
            db.execute_sql(delete_sql)
            db.execute_sql(insert_sql)
            print(f"inserted. data : {data}")


data_dupe_detector(db, table, data_all, column_list_str, column_type)

select_sql = f"SELECT target, actual FROM {table} ORDER BY target"
graph = db.fetch_data_by_sql(select_sql)
target_list = []
actual_list = []
for data in graph:
    target_list.append(data[0])
    actual_list.append(data[1])
plt.plot(target_list, actual_list)
plt.show()
