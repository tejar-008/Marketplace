from django.contrib import admin
from .models import JobListing, CandidatesProfile,SkillSetTrainingModules

# Register your models here.
class JobListingAdmin(admin.ModelAdmin):
    List_display = ['title', 'description']
admin.site.register(JobListing, JobListingAdmin)

class CandidatesProfileAdmin(admin.ModelAdmin):
    List_display = ['specializationinProfession', 'description', 'experience']
admin.site.register(CandidatesProfile, CandidatesProfileAdmin)

class SkillSetTrainingModulesAdmin(admin.ModelAdmin):
    List_display = ['technology', 'description', 'courseDuration','price']
admin.site.register(SkillSetTrainingModules, SkillSetTrainingModulesAdmin)