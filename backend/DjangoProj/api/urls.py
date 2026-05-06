from django.urls import path
from .views import hello, tenders, staff_members, vacancies, apply

urlpatterns = [
    path('hello/', hello),
    path('tenders/', tenders),
    path('staff/', staff_members),
    path('vacancies/', vacancies),
    path('apply/', apply),
]