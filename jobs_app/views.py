from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
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
    job_listings = Job.objects.all()
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


@login_required(login_url='/login/')
def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'GET':
        return render(request, "registration/password_change_form.html", {"form": form})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(
                request, "registration/password_change_done.html", {}
            )
        print(form.errors)
        return render(
            request, "registration/password_change_form.html", {"errors": form.errors}
        )


@login_required(login_url='/login/')
def jobs_list(request):
    all_jobs = Job.objects.all()
    return render(
        request, "jobs_app/jobs_list.html", {"all_jobs": all_jobs, "job_active": "active"}
    )


@login_required(login_url='/login/')
def skills_list(request):
    all_skills = Skill.objects.all()
    return render(
        request, "jobs_app/skill_list.html", {"all_skills": all_skills, "skill_active": "active"}
    )


@login_required(login_url='/login/')
def candidate_list(request):
    all_candidates = CandidatesProfile.objects.all()
    return render(
        request, "jobs_app/candidate_list.html", {"all_candidates": all_candidates, "candidate_active": "active"}
    )


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    profile = CandidatesProfile.objects.filter(user=user)
    return render(
        request, "jobs_app/profile.html", {"profile": profile, "candidate_active": "active"}
    )


@login_required(login_url='/login/')
def add_profile(request):
    form = ProfileForm()
    return render(request, "jobs_app/profile_add.html", {"form": form})
    if request.method == 'POST':
        form = ProfileForm(user=request.user, data=request.POST)
        if form.is_valid():
            print('yooo')
        print(form.errors)
        return render(request, "jobs_app/profile_add.html", {"form": form, 'errors': form.errors})


@login_required(login_url='/login/')
def add_skill(request):
    if request.method == 'GET':
        form = SkillForm()
        return render(request, "jobs_app/add_skill.html", {"form": form})
    if request.method == 'POST':
        form = SkillForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('yesss')
            return HttpResponseRedirect(
                    reverse("jobs_app:skills_list",)
                )
        print(form.errors)
        return render(
            request, "jobs_app/add_skill.html", {"form": form, "errors": form.errors}
        )

@login_required(login_url='/login/')
def add_job(request):
    print('job')
    if request.method == 'GET':
        form = JobForm()
        return render(request, "jobs_app/add_job.html", {"form": form})
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('yesss')
            return HttpResponseRedirect(
                    reverse("jobs_app:jobs_list",)
                )
        print(form.errors)
        return render(
            request, "jobs_app/add_job.html", {"form": form, "errors": form.errors}
        )
