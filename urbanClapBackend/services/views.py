from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Services

from .serializers import ServicesSerializer


class ServicesViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request):
        serReq = ServicesSerializer(data=request.data)
        serReq.is_valid(raise_exception=True)
        serReq.save()
        return Response(serReq.data, status=status.HTTP_200_OK)

    @staticmethod
    def update(request, id):
        serReq = Services.objects.get(id=id)
        serReq.provider_id = ''
        serReq.status = 'ACCEPTED'
        serReq.save()
        serializer = ServicesSerializer(serReq)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def getServiceRequest(request, id):
        serReq = Services.objects.get(id=id)
        serializer = ServicesSerializer(serReq)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def getAllServiceRequests(request, id):
        serReq = Services.objects.get(client_id=id)
        serializer = ServicesSerializer(serReq)
        return Response(serializer.data, status=status.HTTP_200_OK)