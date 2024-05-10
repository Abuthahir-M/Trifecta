from django.urls import path
from . import views

app_name = 'jobtracker'
urlpatterns = [
    path('job-home/', views.jobTracker, name='job-home'),
]