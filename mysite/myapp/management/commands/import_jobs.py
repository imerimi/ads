import csv
from myapp.models import Jobs
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Jobs.objects.create(
                    title=row['title'],
                    company=row['company'],
                    location=row['location'],
                    category=row['category'],
                    jobtype=row['jobtype'],
                    salary=row['salary'],
                    jd=row['jd'],
                    avgsalary=float(row['avgsalary'])
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
