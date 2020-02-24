from django import forms
from jobs_app.models import Skill, Job, CandidatesProfile


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["technology", 'description', 'courseDuration', 'price']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", 'description']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CandidatesProfile
        fields = ["user", 'technology', 'title', 'experience', 'resume', 'description', 'specializedIn']
