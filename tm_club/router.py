from django.shortcuts import render

# Create your views here.
from django.urls import include, re_path as url
from rest_framework import routers

from tm_club.views.club import ClubView
from tm_club.views.division import DivisionView


app_name = "tm_club"
router = routers.SimpleRouter(trailing_slash=False)
router.register(r"^", ClubView, basename="club")
router.register(r"division", DivisionView, basename="division")

urlpatterns = [
    url(r"^", include(router.urls)),
]
