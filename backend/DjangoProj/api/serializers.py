from rest_framework import serializers
from .models import Vacancy, JobApplication


class VacancySerializer(serializers.ModelSerializer):
    employmentType = serializers.CharField(source='employment_type')
    isNew = serializers.BooleanField(source='is_new')
    skills = serializers.SerializerMethodField()
    detailsLink = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'company', 'location', 'salary', 'employmentType',
                  'experience', 'isNew', 'skills', 'detailsLink']

    def get_skills(self, obj):
        return [s.strip() for s in obj.skills.split('\n') if s.strip()]

    def get_detailsLink(self, obj):
        return f'/vacancies/{obj.id}'


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['created_at']
