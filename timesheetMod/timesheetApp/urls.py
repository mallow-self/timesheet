from django.urls import path
from . import views

app_name="timesheet"
urlpatterns = [
    path("", views.index, name="index"),
    path("data", views.enter_data, name="enter_data"),
]
