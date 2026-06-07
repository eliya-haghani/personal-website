from django.urls import path, include
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
path("blog/", include(("blog.urls", "blog"), namespace="blog")),
    path("test/", views.test, name="test"),

]
