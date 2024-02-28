from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     jobs= Job.objects.all()
#     return render(request,'myapp/index.html',{'jobs':jobs})

def index(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 30)  # 30 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/index.html', {'page_obj': page_obj})


def dashboard(request):
    jobs = Job.objects.all()
    return render(request,'myapp/dashboard.html',{'jobs':jobs})
