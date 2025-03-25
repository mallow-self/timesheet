from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async
from .models import Entry
from .forms import EntryForm


@csrf_exempt
async def delete_entry(request: HttpRequest, entry_id: int) -> JsonResponse:
    """Asynchronously deletes an Entry object given its ID if the request method is DELETE."""
    if request.method == "DELETE":
        entry = await Entry.objects.aget(entry_id=entry_id)
        await sync_to_async(entry.delete)()  # Wrap delete in sync_to_async
        return JsonResponse({"success": True, "message": "Entry deleted successfully!"})

    return JsonResponse({"error": "Invalid request method"}, status=400)


async def entry_form(request: HttpRequest) -> HttpResponse | JsonResponse:
    """Handles the creation of a new Entry using Django ModelForm asynchronously."""
    if request.method == "POST":
        form = EntryForm(request.POST)
        if sync_to_async(form.is_valid)():
            await sync_to_async(form.save)()  # Wrap save in sync_to_async
            return redirect("timesheet:index2")

        return JsonResponse({"message": "Invalid data", "errors": form.errors})

    form = EntryForm()
    context = {"form": form}
    return await sync_to_async(render)(request, 'timesheetApp/entryForm.html', context)


def update_entry2(request: HttpRequest, entry_id: int) -> HttpResponse | JsonResponse:
    """Handles updating an existing Entry object asynchronously."""
    entry = Entry.objects.get(entry_id=entry_id)

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save() 
            return redirect("timesheet:index2")

        return JsonResponse({"message": "Invalid data", "errors": form.errors})

    form = EntryForm(instance=entry)
    context = {"form": form, "entry": entry}
    return render(request, "timesheetApp/updateForm.html", context)

async def index2(request: HttpRequest) -> HttpResponse:
    """
    Renders the main index2.html page asynchronously.
    """
    return await sync_to_async(render)(request, "timesheetApp/index2.html")
