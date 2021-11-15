import json

from Manager.Docker.containers import container_logs, container_stop, container_remove
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
    temp_list = manager.container_list()
    for tmp in temp_list:
        print(tmp.id)
        print(tmp.image)
        print(tmp.labels)
        print(tmp.name)
        print(tmp.status)
        print(tmp.id)
    print(manager.container_list(filters={"label": "manager_container=True"}))
    print(manager.container_list(filters={"label": "manager_container"}))
    print(manager.container_list())

    container_stop(container)
    container_remove(container)
    print("for end -------------------------------------------------------")
