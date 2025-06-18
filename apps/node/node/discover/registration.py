from abc import ABC
from os import environ


class NodeRegistration(ABC):
    def __init__(self, id: str, host: str, port: int):
        self.id = id
        self.host = host
        self.port = port

    @property
    def url(self) -> str:
        return f"http://{self.id}:{self.port}"

    def serialize(self):
        return {"id": self.id, "host": self.host, "port": self.port}


class MyRegistration(NodeRegistration):
    def __init__(self):
        id = environ["NODE_ID"]
        host = environ["HOST"]
        port = int(environ["PORT"])
        super().__init__(id, host, port)
