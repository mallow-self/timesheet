from django.urls import path
from . import views

app_name = "timesheet"
urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.enter_data, name="enter_data"),
    path("getProjects/", views.get_projects, name="get_projects"),
    path("getModules/",views.get_modules,name="get_modules"),
    path("getTasks/",views.get_tasks,name="get_tasks"),
    path("entries/",views.get_entries,name="get_entries")
]
