# from django.conf.urls import url
from django.urls import path

from django.contrib.auth import views as auth_views

from jobs_app.views import *

app_name = "jobs_app"
urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("", homepage, name="homepage"),
    path("change-password/", change_password, name="change_password"),
    path("jobs/list/", jobs_list, name="jobs_list"),
    path("candidate/list/", candidate_list, name="candidate_list"),
    path("skills/list/", skills_list, name="skills_list"),
    path("profile/", profile, name="profile"),
    path("profile/add/", add_profile, name="add_profile"),
    path("jobs/add/", add_job, name="add_job"),
    path("skill/add/", add_skill, name="add_skill"),
    
    # path("list/", profile_list, name="admin_homepage"),

]