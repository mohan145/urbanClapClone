from django.urls import path
from .views import UserViewSet


urlpatterns = [
    path('user/create', UserViewSet.as_view({"post": "create"}),),
    path('user/update/<str:id>', UserViewSet.as_view({"post": "update"}),),
    path('user/<str:id>', UserViewSet.as_view({"get": "getUser"}),),
    path('user/locality/<str:locality>', UserViewSet.as_view({"get": "getUserByLocality"}),)
]

