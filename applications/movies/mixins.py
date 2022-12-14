from rest_framework.response import Response
from rest_framework.decorators import action

from applications.movies import services


class LikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()
