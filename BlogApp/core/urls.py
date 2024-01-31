from django.urls import path
from . import views 

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.signin, name="login"),
    path("logout", views.signout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("update-profile", views.update_profile, name="update_profile"),


]
