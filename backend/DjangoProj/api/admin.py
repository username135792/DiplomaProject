from django.contrib import admin
from .models import Tender, StaffMember, Vacancy, JobApplication, Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name', 'address']


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'branch', 'surname', 'role', 'cabinet_number', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'surname', 'role', 'phone', 'email']
    list_editable = ['order', 'is_active']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'branch', 'location', 'salary', 'is_new', 'is_active', 'created_at']
    list_filter = ['is_active', 'is_new', 'employment_type']
    search_fields = ['title', 'branch']
    list_editable = ['is_active', 'is_new']
    fieldsets = [
        ('Основное', {'fields': ['title', 'branch', 'location', 'salary']}),
        ('Детали', {'fields': ['employment_type', 'experience', 'is_new', 'is_active']}),
        ('Навыки', {'fields': ['skills']}),
    ]


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'vacancy_title', 'email', 'phone', 'created_at']
    list_filter = ['vacancy_title', 'created_at', 'marital_status']
    search_fields = ['last_name', 'first_name', 'email', 'phone']
