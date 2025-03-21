from django.urls import path
from . import views

app_name = "timesheet"
urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.enter_data, name="enter_data"),
    path("getProjects/", views.get_projects, name="get_projects"),
    path("getModules/", views.get_modules, name="get_modules"),
    path("getTasks/", views.get_tasks, name="get_tasks"),
    path("entries/", views.get_entries, name="get_entries"),
    path("entries/delete/<int:entry_id>/", views.delete_entry, name="delete_entry"),
    path("entries/update/<int:entry_id>/", views.update_entry, name="update_entries"),
    path("updateForm/<int:entry_id>/", views.update_form, name="update_form"),
]
