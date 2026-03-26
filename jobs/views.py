from django.shortcuts import render
from .models import JobApplication

# Create your views here.


def job_list(request):
    jobs = JobApplication.objects.all()
    return render(request,"jobs/job_list.html", {"jobs": jobs})
    