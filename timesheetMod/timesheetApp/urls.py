from django.urls import path
from . import views
from . import reads


app_name = "timesheet"
urlpatterns = [
    path("getProjects/", reads.get_projects, name="get_projects"),
    path("getModules/", reads.get_modules, name="get_modules"),
    path("getTasks/", reads.get_tasks, name="get_tasks"),
    # django form-crud views
    path('create/', views.entry_form, name='entry_form'),
    path("entries/", reads.get_entries, name="get_entries"),
    path('',views.index2,name="index2"),
    path('update/<int:entry_id>/', views.update_entry2, name="update_entries2"),
    path("entries/delete/<int:entry_id>/",views.delete_entry, name="delete_entry"),

]
