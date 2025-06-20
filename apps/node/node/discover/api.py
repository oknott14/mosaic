import json

from django.http import HttpRequest
from rest_framework import status, viewsets
from rest_framework.response import Response

from .registration import MyRegistration, NodeRegistration
from .service import DiscoverService


class DiscoverApi(viewsets.ViewSet):
    def __init__(self, discover_service=DiscoverService()):
        self.discover_service = discover_service

    def discover(self, request: HttpRequest):
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        self.discover_service.register(NodeRegistration(*body))
        return Response(MyRegistration().serialize(), status=status.HTTP_202_ACCEPTED)
