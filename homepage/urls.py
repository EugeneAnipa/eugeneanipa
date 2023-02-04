from django.urls import path
from homepage import views

urlpatterns = [
    path("homepage/<name>",views.homepage_there, name="homepage_there"),
    path("", views.home, name="home"),
    
    path("home/", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("blog/", views.gblog, name="gblog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]



