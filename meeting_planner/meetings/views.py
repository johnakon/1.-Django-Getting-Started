from meetings.models import Meeting
from django.shortcuts import redirect, render,  get_object_or_404, redirect 

# from django.forms import modelform_factory

from .models import Meeting, Room

from .forms import MeetingForm

# Create your views here.

def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)

    return render(request, "meetings/detail.html", {"meeting": meeting})

# add a new page that shows a list of all rooms available
def room_list(request):
    return render(request, "meetings/rooms_list.html", 
        {"rooms": Room.objects.all()}
    )

# adding a new meeting by the user

# MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        # form has been submitted, process the data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
        
    else:
        form = MeetingForm()
    
    return render(request, "meetings/new.html", {"form": form})