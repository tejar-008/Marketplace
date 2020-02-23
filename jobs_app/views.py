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

# Create your views here.


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
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(password)
            # import pdb; pdb.set_trace()
            user = authenticate(username=username, password=password)
            if user is None:
                print(user)
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

