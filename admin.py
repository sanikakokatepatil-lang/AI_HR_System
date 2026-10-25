from django.contrib import admin
from .models import Job, Candidate

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'required_skills']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'ai_score', 'created_at']