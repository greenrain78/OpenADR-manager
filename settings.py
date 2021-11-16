import os

from src.Utils.env.env_import import setting_dev_env, get_env_none

CONTAINTER_NAME = f"Open ADR Manager"
"""
docker-compose 에서 입력시 우선 반영
지정 없을시 서버에서 운영시 server_on_docker
아닐시 settings_dev 설정 우선
"""
DB_NickName = os.environ.get(
    'DB_NICKNAME',
    default=setting_dev_env('DB_NickName', default='server_on_docker'))

DATABASES = {
    # docker-compose 에서 직접 기입
    'direct': {
        "database": os.environ.get('DB_NAME'),
        "user": os.environ.get('DB_USER'),
        "password": os.environ.get('DB_PASSWORD'),
        "host": os.environ.get('DB_HOST'),
        "port": os.environ.get('DB_PORT'),
    },
    # 로컬에서 사용하는 DB
    'local': {
        "database": 'openadr',
        "user": 'user',
        "password": '1234',
        "host": "127.0.0.1",
        "port": 11100,
    },
    # docker 내에서 연결
    'server_on_docker': {
        "database": 'openadr',
        "user": 'user',
        "password": '1234',
        "host": 'db',
        "port": 5432,
    },
    'aws': {
        "database": 'openadr',
        "user": 'user',
        "password": '1234',
        "host": "3.38.129.72",
        "port": 11100,
    },
}
# DB 연결 설정
IS_SQL_ECHO = setting_dev_env('IS_SQL_ECHO', default=False)
LOGGER_DB = DATABASES[DB_NickName]

# 테스트 설정 변수 반영
IS_RUN_TEST = setting_dev_env('IS_RUN_TEST', default=True)
IS_TEST_ALL = setting_dev_env('IS_TEST_ALL', default=True)

# main 동작 설정
IS_MAIN_RUNNING = setting_dev_env('IS_MAIN_RUNNING', default=True)
MAIN_INTERVAL = setting_dev_env('MAIN_INTERVAL', default=600)

# 스케줄러 동작 설정
IS_RUN_SCHEDULER = setting_dev_env('IS_RUN_SCHEDULER', default=True)

# 중요한 설정변수 변경 금지
IS_DB_TEST_SKIP = True  # DB를 사용하는 테스트 코드 실행 여부


def return_settings():
    return {
        'CONTAINTER_NAME': CONTAINTER_NAME,
        'IS_SERVER': get_env_none('IS_SERVER'),
        "DB_NickName": DB_NickName,
        # "DATABASES": DATABASES,   # DB 정보는 생략
        "IS_DB_TEST_SKIP": IS_DB_TEST_SKIP,
        "IS_RUN_TEST": IS_RUN_TEST,
        "IS_TEST_ALL": IS_TEST_ALL,
        "IS_MAIN_RUNNING": IS_MAIN_RUNNING,
        "MAIN_INTERVAL": MAIN_INTERVAL,
        "IS_SQL_ECHO": IS_SQL_ECHO,
        "IS_RUN_SCHEDULER": IS_RUN_SCHEDULER,
    }
