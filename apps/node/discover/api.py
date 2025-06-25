from models.node import Node
from models.registry import NodeRegistry

from .service import NodeDiscoverService


class DiscoverApi:
    def __init__(
        self, discover_service=NodeDiscoverService(), node_registry=NodeRegistry()
    ):
        self.node_registry = node_registry
        self.discover_service = discover_service

    # def discover(self, request):
    #     try:
    #         print(f"Discovery request from {request.get_host()}")
    #         node = Node.from_json(request.body)
    #         print(f"Node Created - {node}")
    #         my_node = self.node_registry.register(node)
    #         print(f"Node Registered - sending {my_node}")
    #         return Response(my_node.serialize(), status=status.HTTP_202_ACCEPTED)
    #     except Exception as e:
    #         print(f"Failed to validate node - {e}")
    #         return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
