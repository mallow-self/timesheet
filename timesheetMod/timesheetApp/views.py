from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# import logging

# logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request,"timesheetApp/index.html")

def enter_data(request):
    # logger.info(f"Request: {request}")
    if request.method == "POST":
        description = request.POST.get(
            "description", "No Data Received"
        )  # Safely get data
        print(f"Received description: {description}")  # Print to console
        return HttpResponse(
            f"Received data: {description}"
        )  # Display response in browser
    return HttpResponse("No data received")
