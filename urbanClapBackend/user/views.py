from rest_framework import viewsets, status
from rest_framework.response import Response


from serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):

    def create(self, request):
        userSer = UserSerializer(data=request.data)
        userSer.is_valid(raise_exception=True)
        userSer.save()
        return Response(userSer.data,status=status.HTTP_200_OK)
