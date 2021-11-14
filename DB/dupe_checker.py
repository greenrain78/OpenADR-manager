from datetime import datetime, timedelta
from logging import getLogger
from src.DB.DB_Adapter import DBAdapter

logger = getLogger(__name__)
# 데이터를 가져올 서버의 정보
database = {
    "database": 'ppc',
    "user": 'user',
    "password": '1234',
    "host": "15.165.36.229",
    "port": 12100,
}
db = DBAdapter(name="database", direct=database)
print("hello owo")

select_sql = f"SELECT "


