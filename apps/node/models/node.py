
from os import environ
from pydantic import BaseModel

from ..decorators.singleton import singleton

class Node(BaseModel):
    id: str
    host: str
    port: int

    @property
    def url(self) -> str:
        return f"http://{self.id}:{self.port}"


@singleton
class MyNode(Node):
    def __init__(self):
        id = environ["NODE_ID"]
        host = environ["HOST"]
        port = int(environ["PORT"])
        super().__init__(id=id, host=host, port=port)


@singleton
class BootNode(Node):
    def __init__(self):
            id = environ.get("BOOT_NODE_ID", 'boot-node')
            host = environ.get("BOOT_NODE_HOST", '0.0.0.0' )
            port = int(environ.get("BOOT_NODE_PORT", 3000))
            super().__init__(id=id, host=host, port=port)
