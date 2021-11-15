from typing import Optional

from docker.errors import APIError, NotFound
from docker.models.containers import Container

from Manager.Docker.docker_connect import DockerConnecter


class DockerContainers(DockerConnecter):
    """
    docker 컨테이너 관리
    """

    def container_list(self, filters=None):
        """
        컨테이너 리스트를 조회\n
        현재 실행중인 컨테이너들의 이름을 조회한다.
        """
        results = self.docker_client.containers.list(filters=filters)
        return results

    def container_run(self, name, image) -> Optional[Container]:
        """
        해당 이미지를 기반으로 container을 생성
        :param name: 컨테이너 명
        :param image: 이미지 명
        :return:
        """
        try:
            container = self.docker_client.containers.run(
                image, name=name, detach=True,
                labels={
                    "subsystem_container": "True",
                }
            )
            return container
        except APIError as e:
            if e.status_code == 400:
                print("포멧 오류, 한글을 입력하였습니다.")
            elif e.status_code == 409:
                print("이름 중복")
            elif e.status_code == 409:
                print("해당 이름의 이미지가 존재하지 않습니다.")
            else:
                print("새로운 오류코드 발생")
                print(e)
            return None


def container_stop(container):
    # docker stop
    try:
        container.stop()
    except NotFound as e:
        if e.status_code == 404:
            print("이미 정지된 컨테이너 입니다.")
        else:
            print("새로운 오류코드 발생")
            print(e)
        return None


def container_remove(container):
    # docker rm
    try:
        container.remove()
    except NotFound as e:
        if e.status_code == 404:
            print("이미 삭제된 컨테이너 입니다.")
        else:
            print("새로운 오류코드 발생")
            print(e)
        return None


def container_logs(container):
    # docker attach
    try:
        stream = container.attach(stream=True)
        while True:
            line = next(stream).decode("utf-8")
            print(line)
    except StopIteration:
        print(f'container({container.name}) stopped')
