from django.db import models


class Job(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    jobtype = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    jd= models.CharField(max_length=10000)
    avgsalary = models.FloatField()
    mainloc = models.CharField(max_length=100)