from django.shortcuts import render
from .models import JobListing, CandidatesProfile
from django.contrib.auth import authenticate, login
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
    return render(request, "jobs_app/index.html", {'candidatesprofile': candidatesprofile})


def user_logout(request):
    logout(request)
    return redirect(reverse("common:index"))


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
