from typing import Dict

from ..decorators.singleton import singleton
from ..models.node import BootNode, MyNode, Node


class RegistrationException(Exception):
    def __init__(self, node: Node):
        self.message = f"Failed to register node {node}"


@singleton
class NodeRegistry:
    __registry: Dict[str, Node] = {}
    me: Node = MyNode()

    def __init__(self):
        boot_node = BootNode()

    
        self.register(boot_node)

    def register(self, node: Node) -> Node:
        if node.id not in self.__registry:
            self.__registry[node.id] = node

        return self.me

    def get(self, id: str) -> Node | None:
        return self.__registry.get(id, None)

    def remove(self, id: str) -> bool:
        return self.__registry.pop(id, None) is None

    def list(self):
        return list(self.__registry.values())
