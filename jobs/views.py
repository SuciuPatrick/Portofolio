from django.shortcuts import render, get_object_or_404
from .models import Job


# Create your views here.
def patrick(request):
	jobs = Job.objects #grabs everything from the database
	return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
	job_detail = get_object_or_404(Job, pk=job_id) # every model inside the database has ca unique key(primary key)
	return render(request, 'jobs/home.html')