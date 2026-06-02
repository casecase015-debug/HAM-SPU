from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("policy/", views.policy, name="policy"),
    path("callsign/", views.callsign, name="callsign"),
    path("frequencies/", views.frequencies, name="frequencies"),
    path("project/", views.project, name="project"),
    path("team/", views.team, name="team"),
    path("members/", views.members, name="members"),
]
