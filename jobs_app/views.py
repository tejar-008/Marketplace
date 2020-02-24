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
from django.contrib.auth import get_user_model
User = get_user_model()


def homepage(request):
    job_listings = Job.objects.all()
    candidatesprofile = CandidatesProfile.objects.all()
    return render(request, "jobs_app/index.html", {'candidatesprofile': candidatesprofile, "home_active": "active"})


def user_logout(request):
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
                return render(
                    request,
                    "registration/login.html",
                    {"errors": {"account_error": ["Invalid username or password"]}},
                )

            elif user is not None:
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
    if request.method == 'GET':
        form = ProfileForm()
        return render(request, "jobs_app/profile_add.html", {"form": form})
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("jobs_app:candidate_list",)
            )
        return render(
            request, "jobs_app/profile_add.html", {"form": form, "errors": form.errors}
        )

@login_required(login_url='/login/')
def add_skill(request):
    if request.method == 'GET':
        form = SkillForm()
        return render(request, "jobs_app/add_skill.html", {"form": form})
    if request.method == 'POST':
        form = SkillForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("jobs_app:skills_list",)
            )
        return render(
            request, "jobs_app/add_skill.html", {"form": form, "errors": form.errors}
        )


@login_required(login_url='/login/')
def add_job(request):
    if request.method == 'GET':
        form = JobForm()
        return render(request, "jobs_app/add_job.html", {"form": form})
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("jobs_app:jobs_list",)
            )
        return render(
            request, "jobs_app/add_job.html", {"form": form, "errors": form.errors}
        )

@login_required
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            # login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect(reverse("jobs_app:candidate_list",))
    else:
        form = UserForm()

    return render(request, 'jobs_app/add_user.html', {'form': form})

def delete_skill(request, id):
    skill = Skill.objects.filter(id=id)
    skill.delete()
    return HttpResponseRedirect(reverse("jobs_app:skills_list",))

def delete_profile(request, id):
    candidate = CandidatesProfile.objects.filter(id=id)
    candidate.delete()
    return HttpResponseRedirect(reverse("jobs_app:candidate_list",))

def delete_job(request, id):
    job = Job.objects.filter(id=id)
    job.delete()
    return HttpResponseRedirect(reverse("jobs_app:jobs_list",))