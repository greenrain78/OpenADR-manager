from Manager.Docker.docker_connect import DockerConnecter


class DockerImages(DockerConnecter):

    def build_image(self, path, tag):
        """docker image 생성\n
        dockerfile을 사용하여 docker 이미지를 생성한다.

        :param path: dockerfile 경로
        :param tag: 이미지 이름
        """
        # Build docker image
        print('Building docker image ...')
        streamer = self.docker_api.build(
            decode=True,    # 디코딩해서 보기 쉽게 로그 출력
            forcerm=True,   # 빌드 종료후 사용한 컨테이너 제거
            path=path,
            tag=tag,
        )

        for chunk in streamer:
            if 'stream' in chunk:
                for line in chunk['stream'].splitlines():
                    print(line)
