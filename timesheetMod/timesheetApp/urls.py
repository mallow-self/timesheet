from django.urls import path
from . import views
from . import reads


app_name = "timesheet"
urlpatterns = [
    path("getProjects/", reads.get_projects, name="get_projects"),
    path("getModules/", reads.get_modules, name="get_modules"),
    path("getTasks/", reads.get_tasks, name="get_tasks"),
    # django form views
    path('entry/', views.entryForm, name='entry_form'),
    path("entries/", reads.get_entries, name="get_entries"),
    path('timesheet/',views.index2,name="index2"),
    path('timesheet/updateForm/<int:entry_id>/', views.update_entry2, name="update_entries2"),
    path("entries/delete/<int:entry_id>/",views.delete_entry, name="delete_entry"),

]
