from ..clients.http_client import HttpClient
from ..decorators.singleton import singleton
from ..models.node import Node


@singleton
class NodeDiscoverService(HttpClient):
    def __init__(self):
        super().__init__()
        self.add_retry_strategy()

    def introduce(self, node: Node) -> Node | None:
        try:
            print(f"Making introduction to {node.url}")
            response = self.post(
                f"{node.url}/discover/",
                node,
                {"Content-Type": "application/json"},
                Node
            )

            print(response)
            return response.body
        except Exception as e:
            print(f"Failed to introduce to {node.url} - {e}")
