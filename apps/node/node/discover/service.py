from abc import ABC
from os import environ
from typing import Self

import requests

from .registration import NodeRegistration


class DiscoverService(ABC):
    __instance: Self | None = None
    registry = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if "BOOT_NODE_ID" in environ:
            boot_id = environ["BOOT_NODE_ID"]
            boot_host = environ["BOOT_NODE_HOST"]
            boot_port = int(environ["BOOT_NODE_PORT"])

            self.register(NodeRegistration(boot_id, boot_host, boot_port))

    def introduce(self):
        for registration in self.registry.values():
            print(f"Introduction to {registration.url}")
            response = requests.post(
                f"{registration.url}/discover",
                registration.serialize(),
                headers={"Content-Type": "application/json"},
            )
            self.register(NodeRegistration(*response.json()))

    def register(self, registration: NodeRegistration):
        self.registry[registration.id] = registration
        return True
