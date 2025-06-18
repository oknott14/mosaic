from django.urls import path

from .discover.api import DiscoverApi
from .views import NodeViewSet

urlpatterns = [
    path("health/", NodeViewSet.as_view({"get": "health"})),
    path("discover/", DiscoverApi.as_view({"post": "discover"})),
]
