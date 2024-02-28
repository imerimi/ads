from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    jobs= Job.objects.all()
    return render(request,'myapp/index.html',{'jobs':jobs})


def dashboard(request):
    jobs = Job.objects.all()
    return render(request,'myapp/dashboard.html',{'jobs':jobs})
