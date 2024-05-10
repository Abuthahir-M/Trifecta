from django.shortcuts import render

# Create your views here.

def jobTracker(request):
    return render(request, 'jobtracker/job-home.html')