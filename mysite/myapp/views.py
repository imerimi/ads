from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Avg


def index(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 30)  # 30 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/index.html', {'page_obj': page_obj})


from django.db.models import Avg, Count
from django.shortcuts import render
from .models import Job

def dashboard(request):
    # Retrieve all jobs from the Job model
    jobs = Job.objects.all()
    
    # Calculate the total number of jobs
    total_jobs = jobs.count()
    
    # Retrieve category counts from the Job model
    categories = Job.objects.values('category').annotate(count=Count('category'))
    categories_sorted = sorted(categories, key=lambda x: x['count'], reverse=True)

    # Calculate average salary by main location
    mainloc_avgsalary = (
        Job.objects.exclude(avgsalary=0)
        .values('location')
        .annotate(avg_salary=Avg('avgsalary'))
        .exclude(location='')
    )

    mainloc_avgsalary_list = list(mainloc_avgsalary)

    # Pass the total number of jobs, category counts, and mainloc_avgsalary_list to the template context
    return render(request, 'myapp/dashboard.html', {'total_jobs': total_jobs, 'categories': categories_sorted, 'mainloc_avgsalary_list': mainloc_avgsalary_list})
