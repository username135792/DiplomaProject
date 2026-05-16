from django.urls import path
from .views import hello, tenders, staff_members, vacancies, vacancy_detail, vacancy_filters, apply

urlpatterns = [
    path('hello/', hello),
    path('tenders/', tenders),
    path('staff/', staff_members),
    path('vacancies/<int:pk>/', vacancy_detail),
    path('vacancies/', vacancies),
    path('vacancy-filters/<str:field_name>/', vacancy_filters),
    path('apply/', apply),
]