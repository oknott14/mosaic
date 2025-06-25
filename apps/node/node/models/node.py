import json
from abc import ABC
from dataclasses import dataclass
from os import environ
from typing import Any, Dict

from node.decorators.singleton import singleton


@dataclass
class NodeConnection(ABC):
    host: str
    port: int

    @property
    def is_valid(self):
        return hasattr(self, "host") and hasattr(self, "port")

    def to_json(self):
        return json.dumps(self.__dict__)


class Node(ABC):
    def __init__(self, id: str, connection: NodeConnection):
        self.id = id
        self.connection = connection

    @property
    def url(self) -> str:
        return f"http://{self.id}:{self.connection.port}"

    def serialize(self):
        return {"id": self.id, "connection": self.connection.to_json()}

    @property
    def is_valid(self) -> bool:
        return (
            hasattr(self, "id")
            and hasattr(self, "connection")
            and self.connection.is_valid
        )

    @classmethod
    def from_json(cls, json_string: str | bytes | bytearray):
        data: Dict[str, Any] = json.loads(json_string)

        return cls(data['id'], NodeConnection(*data['connection']))


@singleton
class MyNode(Node):
    def __init__(self):
        id = environ["NODE_ID"]
        host = environ["HOST"]
        port = int(environ["PORT"])
        super().__init__(id=id, connection=NodeConnection(host, port))


@singleton
class BootNode(Node):
    def __init__(self):
        try:
            id = environ["BOOT_NODE_ID"]
            host = environ["BOOT_NODE_HOST"]
            port = int(environ["BOOT_NODE_PORT"])

            super().__init__(id, NodeConnection(host, port))
        except Exception:
            pass
