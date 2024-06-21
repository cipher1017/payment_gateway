from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),

    path("add_comment/", views.add_comment, name="add_comment"),
    path('about/', views.about, name="about"),

]

