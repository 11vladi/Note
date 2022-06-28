from . import views
from django.urls import path

urlpatterns = [
    path("register/", views.register, name="register"),
    path("view_profile/", views.view_my_profile, name="view_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
