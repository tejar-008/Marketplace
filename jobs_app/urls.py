# from django.conf.urls import url
from django.urls import path

from django.contrib.auth import views as auth_views

from jobs_app.views import *

app_name = "jobs_app"
urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("signup/", user_signup, name="user_signup"),
    path("", homepage, name="homepage"),
    path("change-password/", change_password, name="change_password"),
    path("jobs/list/", jobs_list, name="jobs_list"),
    path("candidate/list/", candidate_list, name="candidate_list"),
    path("skills/list/", skills_list, name="skills_list"),
    path("profile/", profile, name="profile"),
    path("profile/add/", add_profile, name="add_profile"),
    path("jobs/add/", add_job, name="add_job"),
    path("skill/add/", add_skill, name="add_skill"),
    path("user/add/", add_user, name="add_user"),
    path("profile/delete/<int:id>/", delete_profile, name="delete_profile"),
    path("jobs/delete/<int:id>/", delete_job, name="delete_job"),
    path("skill/delete/<int:id>/", delete_skill, name="delete_skill"),
    path("skill/edit/<int:id>/", edit_skill, name="edit_skill"),
    path("jobs/edit/<int:id>/", edit_job, name="edit_job"),
    path("profile/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("user/edit/<int:id>/", edit_user, name="edit_user"),
    
    # path("list/", profile_list, name="admin_homepage"),

]