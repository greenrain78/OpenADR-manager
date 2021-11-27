import os

# 컨테이너 명
CONTAINTER_NAME = os.environ.get('CONTAINTER_NAME', default='local')

DB_NICKNAME = os.environ.get(
    'DB_NICKNAME',  # 환경변수로 우선 입력
    default='local')  # 지정 없을시 서버에서 운영시 server_on_docker
IS_MAIN_RUNNING = True  # main 함수 계속 동작 여부
MAIN_INTERVAL = 3600

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
