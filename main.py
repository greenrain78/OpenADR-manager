import traceback
from logging import getLogger
from time import sleep

from pycontainerutils.db.BaseDB_Adapter import BaseDBAdapter
from pycontainerutils.logger.setting_logger import Log_settings

from Manager.Controller.logger_config import main_loggers_config
from settings import CONTAINTER_NAME, DATABASES, DB_NICKNAME, IS_MAIN_RUNNING, MAIN_INTERVAL

logger = getLogger(__name__)

if __name__ == '__main__':
    print(f"{CONTAINTER_NAME}: logger settings")

    # 로그 설정
    Log_settings.logger_settings(
        logger_config=main_loggers_config,
        container_name=CONTAINTER_NAME,
        db_info=DATABASES[DB_NICKNAME]
    )
    # db 설정
    BaseDBAdapter.init_settings(
        databases=DATABASES,
        default_db_name=DB_NICKNAME,
        # is_echo_sql="debug",
        is_echo_sql=False,
    )
    logger.info(f"{CONTAINTER_NAME}:  run main")

    try:
        from Manager.manager import manager_start
        manager_start()
        pass
    except Exception as e:

        logger.error(f"{CONTAINTER_NAME}: main running error\n"
                     f"{traceback.format_exc()}")

    # main 동작 유지
    while IS_MAIN_RUNNING:
        logger.debug(f"{CONTAINTER_NAME}: running main process")
        sleep(MAIN_INTERVAL)

    logger.info(f"{CONTAINTER_NAME}: end main")