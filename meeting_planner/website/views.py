from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
# def welcome(request):
#     # return HttpResponse("Welcome aboard! This is the Meeting Planner.")
#     return render(request, "website/welcome.html", 
#         {"message": " This data was sent from the view to the template"}
#     )

def welcome(request):
    return render(request, "website/welcome.html", 
        {"num_meetings": Meeting.objects.count()}  # template context
    )

def date(request):
    return HttpResponse("This page is serverd at " + str(datetime.now()))

def about(request):
    return HttpResponse("About : Meeting Planner")

