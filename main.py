import traceback
from logging import getLogger
from time import sleep

from Manager.Controller.logger_config import main_loggers_config
from Manager.manager import manager_start
from settings import CONTAINTER_NAME, LOGGER_DB, DATABASES, IS_SQL_ECHO, DB_NickName, return_settings, IS_MAIN_RUNNING, \
    MAIN_INTERVAL
from src.DB.BaseDB_Adapter import BaseDBAdapter
from src.Logger.db.DB_handler import DatabaseHandler
from src.Logger.setting_logger import log_settings

logger = getLogger(__name__)

project_name = f"openadr manager"

if __name__ == '__main__':
    print(f"{project_name}: logger settings")
    log_settings.logger_settings(logger_config=main_loggers_config)
    DatabaseHandler.init_db_adapter(container=CONTAINTER_NAME, db_info=LOGGER_DB)


    logger.info(f"{project_name}: db adapter setting")
    BaseDBAdapter.init_settings(databases=DATABASES, is_echo_sql=IS_SQL_ECHO, db_name=DB_NickName)
    # DB 로거 생성

    logger.info(f"{project_name}: print settings")
    for key, val in return_settings().items():
        print(f"{key}, {val}")
    logger.info(f"{project_name}: run main")


    try:
        # main run
        manager_start()
    except Exception as e:

        logger.error(f"{project_name}: main running error\n"
                     f"{traceback.format_exc()}")

    # main 동작 유지
    while IS_MAIN_RUNNING:
        logger.debug(f"{project_name}: running main process")
        sleep(MAIN_INTERVAL)

    logger.info(f"{project_name}: end main")
