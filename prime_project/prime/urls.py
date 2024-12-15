from django.urls import path
from .views import prime_range

urlpatterns = [
    path('basic/primerange/', prime_range, name='prime_range'),
]
