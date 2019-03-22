from django.shortcuts import render
from .models import Job


# Create your views here.
def patrick(request):
	jobs = Job.objects #grabs everything from the database
	return render(request, 'jobs/home.html', {'jobs': jobs})