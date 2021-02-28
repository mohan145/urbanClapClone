from django.urls import path
from .views import NotifyViewSet


urlpatterns = [
    path('notify/create', NotifyViewSet.as_view({"post": "create"}), ),
    path('notify/update/<str:id>', NotifyViewSet.as_view({"post": "update"}),),
    path('notify/<str:id>', NotifyViewSet.as_view({"get": "getNotification"}), ),
]

