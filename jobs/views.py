from django.shortcuts import render, redirect
from .models import JobApplication

# Create your views here.


def job_list(request):
    jobs = JobApplication.objects.all()
    return render(request,"jobs/job_list.html", {"jobs": jobs})
    

def create_job(request):
    if request.method== "POST":
        company = request.POST.get("company")
        position = request.POST.get("position")
        
        JobApplication.objects.create(
            company=company,
            position=position
)
        return redirect("/")


    return render(request, "jobs/create_job.html")