from django.urls import path
from .views import hello, vacancies, apply

urlpatterns = [
    path('hello/', hello),
    path('vacancies/', vacancies),
    path('apply/', apply),
]