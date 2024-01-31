from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<slug:slug>", views.detail, name="detail"),
    path("create/article", views.create_article, name="create_article"),

]
