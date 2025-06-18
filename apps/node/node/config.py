from os import environ

from django.apps import AppConfig

from .discover.service import DiscoverService


class NodeAppConfig(AppConfig):
    name = "node"
    verbose_name = "Node App Config"

    def ready(self):
        print("SERVER LIVE - INTRODUCING NODES")
        if "BOOT_NODE" not in environ or environ["BOOT_NODE"] != "1":
            discovery = DiscoverService()
            discovery.introduce()
