from django.apps import AppConfig

from node.discover.service import NodeDiscoverService
from node.models.registry import NodeRegistry


class NodeAppConfig(AppConfig):
    name = "node"
    verbose_name = "Node App Config"
    initialized: bool = False
    registry = NodeRegistry()
    discovery_service = NodeDiscoverService()

    def ready(self):
        if hasattr(self, "_ready_executed"):
            return
        self._ready_executed = True
        self.check_node_connections()

    def check_node_connections(self):
        print("Checking Node Connections")

        for node in self.registry.list():
            response = self.discovery_service.introduce(node)
            if response is not None:
                self.registry.register(response)
