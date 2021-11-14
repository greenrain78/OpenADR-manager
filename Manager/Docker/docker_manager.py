import docker

from Manager.Docker.containers import DockerContainers
from Manager.Docker.images import DockerImages


class DockerManager(DockerContainers, DockerImages):

    def __init__(self):
        super().__init__()

    def docker_client_events(self):
        events = self.docker_client.events(decode=True)
        for event in events:
            print(event)
