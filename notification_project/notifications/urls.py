from django.urls import path
from .views import list_notifications

urlpatterns = [
    path('tasks/listnotifications/<str:member_id>/', list_notifications, name='list_notifications'),
]
