from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Notify

from .serializers import NotifySerializer


class NotifyViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request):
        ntfy = NotifySerializer(data=request.data)
        ntfy.is_valid(raise_exception=True)
        ntfy.save()
        return Response(ntfy.data, status=status.HTTP_200_OK)

    @staticmethod
    def update(request, id):
        ntfy = Notify.objects.get(id=id)
        ntfy.type = 'APPROVAL'
        ntfy.save()
        serializer = NotifySerializer(ntfy)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def getNotification(request, id):
        ntfy = Notify.objects.get(id=id)
        serializer = NotifySerializer(ntfy)
        return Response(serializer.data, status=status.HTTP_200_OK)