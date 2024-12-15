from django.urls import path
from .views import prime_checker

urlpatterns = [
    path('', prime_checker, name='prime_checker'),
]
