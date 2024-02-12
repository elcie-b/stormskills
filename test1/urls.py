from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard),
    path("log/", views.log)
]
