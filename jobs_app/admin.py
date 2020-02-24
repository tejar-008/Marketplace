from django.contrib import admin
from .models import Job, CandidatesProfile, Skill, User

# Register your models here.


class JobListingAdmin(admin.ModelAdmin):
    List_display = ['title', 'description']


admin.site.register(Job)


class CandidatesProfileAdmin(admin.ModelAdmin):
    List_display = ['specializationinProfession', 'description', 'experience']


admin.site.register(CandidatesProfile, CandidatesProfileAdmin)


class SkillsAdmin(admin.ModelAdmin):
    List_display = ['technology', 'description', 'courseDuration', 'price']


admin.site.register(Skill)


admin.site.register(User)