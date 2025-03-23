from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Entry, Project, Module, Task
from django.views.decorators.csrf import csrf_exempt


# This file is entirely for read operations

def get_projects(request):
    projects = list(Project.objects.all().values("project_id", "name"))
    responseData = {"projects": projects}
    return JsonResponse(responseData)


def get_modules(request):
    # Get project_id from query params
    project_id = request.GET.get("project_id")
    if not project_id:
        return JsonResponse({"error": "project_id is required"}, status=400)

    modules = list(
        Module.objects.filter(project_id=project_id).values(
            "module_id", "name")
    )
    return JsonResponse({"modules": modules})


def get_tasks(request):
    module_id = request.GET.get("module_id")
    if not (module_id):
        return JsonResponse(
            {"error": "project_id is required and module_id is required"}, status=400
        )

    tasks = list(Task.objects.filter(
        module_id=module_id).values("task_id", "name"))
    return JsonResponse({"tasks": tasks})


def get_entries(request):
    entries = list(
        Entry.objects.all()
        .values(
            "entry_id",
            "date_entry",
            "description",
            "project__name",
            "module__name",
            "task__name",
            "time_entry",
        )
        .order_by("-date_entry")
    )
    responseData = {"entries": entries}
    return JsonResponse(responseData)