from django.urls import path
from .views import hello, staff_members, vacancies, apply

urlpatterns = [
    path('hello/', hello),
    path('staff/', staff_members),
    path('vacancies/', vacancies),
    path('apply/', apply),
]