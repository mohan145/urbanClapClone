from django.urls import path
from .views import ServicesViewSet


urlpatterns = [
    path('services/create', ServicesViewSet.as_view({"post": "create"}), ),
    path('services/update/<str:id>', ServicesViewSet.as_view({"post": "update"}),),
    path('services/<str:id>', ServicesViewSet.as_view({"get": "getServiceRequest"}), ),
    path('services/user/<str:id>', ServicesViewSet.as_view({"get": "getAllServiceRequests"}), ),
]

