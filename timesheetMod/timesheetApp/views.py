from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Entry, Project, Module, Task
from django.views.decorators.csrf import csrf_exempt
from .forms import EntryForm

# Create your views here.

@csrf_exempt
def delete_entry(request, entry_id):
    if request.method == "DELETE":
        entry = get_object_or_404(Entry, entry_id=entry_id)
        entry.delete()
        return JsonResponse({"success": True, "message": "Entry deleted successfully!"})

    return JsonResponse({"error": "Invalid request method"}, status=400)

#django model form
def entryForm(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            # save the data to entry module
            form.save()
            return redirect("timesheet:index2")
        else:
            print("Form errors:", form.errors)  # Debugging line
            return JsonResponse({"message": "Invalid data", "errors": form.errors})
    form = EntryForm()
    context = {"form": form}
    return render(request, 'timesheetApp/entryForm.html',context=context)

def index2(request):
    return render(request, "timesheetApp/index2.html")

def update_entry2(request,entry_id):
    # Ensure correct lookup field
    entry = get_object_or_404(Entry, entry_id=entry_id)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect("timesheet:index2")
        else:
            print("Form errors:", form.errors)  # Debugging line
            return JsonResponse({"message": "Invalid data", "errors": form.errors})

    form = EntryForm(instance=entry)
    context = {"form": form, "entry": entry}
    return render(request, "timesheetApp/updateForm.html", context)
