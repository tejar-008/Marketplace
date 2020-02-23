# from django.conf.urls import url
from django.urls import path

from django.contrib.auth import views as auth_views

from jobs_app.views import *

app_name = "jobs_app"
urlpatterns = [
    path("", homepage, name="homepage"),
    # path("list/", profile_list, name="admin_homepage"),
    # path("", profile_view, name="admin_homepage"),
    path("logout/", user_logout, name="user_logout"),
    path("login/", user_login, name="user_login"),


]