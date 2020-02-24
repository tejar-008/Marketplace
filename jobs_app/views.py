from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import (
    # HttpResponse,
    HttpResponseRedirect,
    redirect,
    render,
    reverse,
)
from jobs_app.forms import *
from django.contrib.auth.forms import PasswordChangeForm


def homepage(request):
    job_listings = JobListing.objects.all()
    candidatesprofile = CandidatesProfile.objects.all()
    return render(request, "jobs_app/index.html", {'candidatesprofile': candidatesprofile, "home_active": "active"})


def user_logout(request):
    print('logout')
    logout(request)
    return redirect(reverse("jobs_app:user_login"))


def user_login(request):
    if request.method == "GET":
        return render(request, "registration/login.html", {})

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is None:
                print(user)
                return render(
                    request,
                    "registration/login.html",
                    {"errors": {"account_error": ["Invalid username or password"]}},
                )

            elif user is not None:
                print('not none')
                login(request, user)
                return HttpResponseRedirect(
                    reverse("jobs_app:homepage",)
                )
        else:
            return render(
                request, "registration/login.html", {"errors": form.errors}
            )


def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'GET':
        return render(request, "registration/password_change_form.html", {"form": form})
    if form.is_valid():
        form.save()
        return render(
            request, "registration/password_change_done.html", {}
        )
    return render(
        request, "registration/password_change_done.html", {"errors": form.errors}
    )


def jobs_list(request):
    all_jobs = JobListing.objects.all()
    return render(
        request, "jobs_app/jobs_list.html", {"all_jobs": all_jobs, "job_active": "active"}
    )


def skills_list(request):
    all_skills = SkillSetTrainingModules.objects.all()
    return render(
        request, "jobs_app/skill_training_list.html", {"all_skills": all_skills, "skill_active": "active"}
    )


def candidate_list(request):
    all_candidates = CandidatesProfile.objects.all()
    return render(
        request, "jobs_app/candidate_list.html", {"all_candidates": all_candidates, "candidate_active": "active"}
    )


def profile(request):
    user = request.user
    profile = CandidatesProfile.objects.filter(user=user)
    return render(
        request, "jobs_app/profile.html", {"profile": profile, "candidate_active": "active"}
    )
