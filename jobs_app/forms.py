from django import forms
from jobs_app.models import Skill, Job, CandidatesProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')