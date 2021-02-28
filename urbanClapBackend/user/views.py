from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User


from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request):
        userSer = UserSerializer(data=request.data)
        userSer.is_valid(raise_exception=True)
        userSer.save()
        return Response(userSer.data,status=status.HTTP_200_OK)


    @staticmethod
    def update(request, id):
        user = User.objects.get(id=id)
        user.availability = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @staticmethod
    def getUser(request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @staticmethod
    def getUserByLocality(request, locality):
        users = User.objects.filter(locality=locality,availability=True,user_type='SERVICE_PROVIDER')
        if users:
            user = users[0]
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


