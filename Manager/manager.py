import json

from Manager.Docker.containers import container_logs, container_stop
from Manager.Docker.docker_manager import DockerManager
import logging

logger = logging.getLogger(__name__)


def manager_start():
    print("main run")
    logger.info("main run")


    manager = DockerManager()
    print(manager.container_list())
    manager.build_image(path='Model', tag="test/adw")
    container = manager.container_run(name="test123", image="test/adw")
    print("build end")
    print(type(container))

    print("1234")
    print("for end -------------------------------------------------------")
