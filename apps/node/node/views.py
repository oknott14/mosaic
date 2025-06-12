from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

class NodeViewSet(viewsets.ViewSet):

  def health(self, request):
    return Response({ 'success': True }, status = status.HTTP_200_OK)