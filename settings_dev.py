DEV_SETTINGS = {
    # DB 연결 설정
    "DB_NickName": 'local',     # 연결할 DB
    "IS_SQL_ECHO": True,        # SQL문 출력

    # 테스트 설정 변수 반영
    "IS_RUN_TEST": False,       # 테스트 실행
    "IS_TEST_ALL": True,        # 테스트 코드 전체 실행, false시 일부 지정된 테스트 코드만 실행

    # main 동작 설정
    "IS_MAIN_RUNNING": False,   # main 함수 계속 동작 여부
    "MAIN_INTERVAL": 10,

    # 스케줄러 동작 설정
    "IS_RUN_SCHEDULER": False,   # 스케줄러 실행 여부

}

LOGGER_SETTINGS = {
    # 로그 출력 수준 설정: DEBUG - 모든 로그 출력, INFO - 알림 로그만 출력
    "CONSOLE_HANDLER_LEVEL": "DEBUG",
    # 스케줄러 로그 출력 수준 설정
    "SCHEDULE_LOGGER_LEVEL": "DEBUG",
}
