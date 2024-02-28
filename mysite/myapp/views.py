from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from django.db.models import Count
import geopandas as gpd
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
    # Retrieve all jobs from the Job model
    jobs = Job.objects.all()
    
    # Calculate the total number of jobs
    total_jobs = jobs.count()
    
    # Retrieve category counts from the Job model
    categories = Job.objects.values('category').annotate(count=Count('category'))

    categories_list = list(categories)

    categories_sorted = sorted(categories_list, key=lambda x: x['count'], reverse=True)




    # Pass the total number of jobs and category counts to the template context
    return render(request, 'myapp/dashboard.html', {'total_jobs': total_jobs, 'categories': categories_sorted})