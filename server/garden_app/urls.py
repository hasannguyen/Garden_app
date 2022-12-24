from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # API ROUTES FOR USER
    path("api/signIn/", views.signIn)
]
