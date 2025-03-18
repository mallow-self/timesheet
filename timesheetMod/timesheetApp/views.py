from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Entry, Project, Module, Task
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "timesheetApp/index.html")


def enter_data(request):
    if request.method == "POST":
        try:
            date_entry = request.POST.get("date")
            description = request.POST.get("description")
            project_id = request.POST.get("project")
            module_id = request.POST.get("module")
            task_id = request.POST.get("task")
            time_entry = request.POST.get("time")

            if not all(
                [date_entry, description, project_id, module_id, task_id, time_entry]
            ):
                return JsonResponse({"error": "All fields are required"}, status=400)
            # Fetch related objects
            project = get_object_or_404(Project, project_id=project_id)
            module = get_object_or_404(Module, module_id=module_id)
            task = get_object_or_404(Task, task_id=task_id)

            # Convert time_entry to integer
            time_entry = int(time_entry) if time_entry.isdigit() else 0

            # check if task,module and project match
            if int(task.module.module_id) == int(module_id) and int(
                task.module.project.project_id
            ) == int(project_id):
                # Create and save the Entry object
                entry = Entry.objects.create(
                    date_entry=date_entry,
                    description=description,
                    project=project,
                    module=module,
                    task=task,
                    time_entry=time_entry,
                )

                return redirect("timesheet:index")
            else:
                return JsonResponse({"message:": "Invalid Project-Module-Task!"})

        except Exception as e:
            return JsonResponse({"server-error": f"{e}"})

    return JsonResponse({"error": "Invalid request"}, status=400)


def get_projects(request):
    projects = list(Project.objects.all().values("project_id", "name"))
    responseData = {"projects": projects}
    return JsonResponse(responseData)


def get_modules(request):
    project_id = request.GET.get("project_id")  # Get project_id from query params
    if not project_id:
        return JsonResponse({"error": "project_id is required"}, status=400)

    modules = list(
        Module.objects.filter(project_id=project_id).values("module_id", "name")
    )
    return JsonResponse({"modules": modules})


def get_tasks(request):
    module_id = request.GET.get("module_id")
    if not (module_id):
        return JsonResponse(
            {"error": "project_id is required and module_id is required"}, status=400
        )

    tasks = list(Task.objects.filter(module_id=module_id).values("task_id", "name"))
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


@csrf_exempt
def delete_entry(request, entry_id):
    if request.method == "DELETE":
        entry = get_object_or_404(Entry, entry_id=entry_id)
        entry.delete()
        return JsonResponse({"success": True, "message": "Entry deleted successfully!"})

    return JsonResponse({"error": "Invalid request method"}, status=400)


def update_entry(request, entry_id):
    entry = get_object_or_404(Entry, entry_id=entry_id)
    if request.method == "POST":
        try:
            date_entry = request.POST.get("date")
            description = request.POST.get("description")
            project_id = request.POST.get("project")
            module_id = request.POST.get("module")
            task_id = request.POST.get("task")
            time_entry = request.POST.get("time")

            if not all(
                [date_entry, description, project_id, module_id, task_id, time_entry]
            ):
                return JsonResponse({"error": "All fields are required"}, status=400)
            # Fetch related objects
            project = get_object_or_404(Project, project_id=project_id)
            module = get_object_or_404(Module, module_id=module_id)
            task = get_object_or_404(Task, task_id=task_id)

            # Convert time_entry to integer
            time_entry = int(time_entry) if time_entry.isdigit() else 0

            # check if task,module and project match
            if int(task.module.module_id) == int(module_id) and int(task.module.project.project_id) == int(project_id):
                # Update the todo object
                entry.date_entry = date_entry
                entry.description = description
                entry.project = project
                entry.module = module
                entry.task = task
                entry.time_entry = time_entry
                entry.save()

                return redirect("timesheet:index")
            else:
                return JsonResponse({"message:": "Invalid Project-Module-Task!"})

        except Exception as e:
            return JsonResponse({"server-error": f"{e}"})

    return JsonResponse({"error": "Invalid request"}, status=400)

def update_form(request,entry_id):
    try:
        entry = get_object_or_404(Entry, entry_id=entry_id)
        date_entry_str = entry.date_entry.strftime("%Y-%m-%d") if entry.date_entry else ""
        time_entry_id:int = 0
        if entry.time_entry % 15 == 0:
            time_entry_id = int(entry.time_entry // 15)
        context = {
            "entry_id": entry.entry_id,
            "date_entry": date_entry_str,
            "description": entry.description,
            "project":entry.project,
            "module":entry.module.name,
            "task":entry.task,
            "time_entry":entry.time_entry,
        }
        return render(request, "timesheetApp/update.html", context)
    except Exception as e:
        return JsonResponse({"Exception Occurred:": f"{e}"})
