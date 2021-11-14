import docker


class DockerConnecter:

    def __init__(self):
        self.docker_client = docker.from_env()
        # Low-level API
        self.docker_api = docker.APIClient(base_url='unix://var/run/docker.sock')

