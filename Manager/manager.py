
def manager_start():
    print("main run")
    import docker
    client = docker.from_env()
    print(client)
    for container in client.containers.list():
        print(container.name)

    print("for end -------------------------------------------------------")
