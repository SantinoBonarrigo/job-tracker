from django.shortcuts import render, redirect
from .models import JobApplication

# Create your views here.

def edit_job(request, job_id):
    job = JobApplication.objects.get(id=job_id)

    if request.method == "POST":
        job.company = request.POST.get("company")
        job.position = request.POST.get("position")
        job.save()
        return redirect("/")

    return render(request, "jobs/edit_job.html", {"job": job})

       



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


def delete_job(request,job_id):
    job= JobApplication.objects.get(id=job_id)

    if request.method == "POST":
     job.delete()
     return redirect("/")

    return render(request, "jobs/delete_job.html", {"job": job})

        
       


