from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_view, name="blog"),
    path("<int:pid>/", views.blog_single, name="single"),
]