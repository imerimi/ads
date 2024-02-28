from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Avg
from wordcloud import WordCloud
import io
import base64

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

    jobtypes = Job.objects.values('jobtype').annotate(count=Count('jobtype'))
    jobtype_sorted = sorted(jobtypes, key=lambda x: x['count'], reverse=True)

    # Calculate average salary by main location
    mainloc_avgsalary = (
        Job.objects.exclude(avgsalary=0)
        .values('location')
        .annotate(avg_salary=Avg('avgsalary'))
        .exclude(location='')
    )

    category_avg_salary = (
        Job.objects.exclude(avgsalary=0)
        .values('category')
        .annotate(avg_salary=Avg('avgsalary'))
    )


    mainloc_avgsalary_list = list(mainloc_avgsalary)

    category_avg_salary_list= list(category_avg_salary)

     # Retrieve job descriptions from the database
    job_descriptions = Job.objects.values_list('jd', flat=True)

    # Assuming you have retrieved job descriptions and concatenated them into a single string
    text = " ".join(job_descriptions)

    # Set the width and height parameters when creating the WordCloud object
    wordcloud = WordCloud(width=800, height=600, background_color='white').generate(text)

    # Convert the word cloud image to a PNG format
    image_stream = io.BytesIO()
    wordcloud.to_image().save(image_stream, format='PNG')
    image_stream.seek(0)
    image_data = base64.b64encode(image_stream.getvalue()).decode()


    # Pass the total number of jobs, category counts, and mainloc_avgsalary_list to the template context
    return render(request, 'myapp/dashboard.html', {'total_jobs': total_jobs, 'categories': categories_sorted, 'mainloc_avgsalary_list': mainloc_avgsalary_list, 'category_avg_salary': category_avg_salary_list,'jobtypes': jobtype_sorted,'wordcloud_image': image_data})
