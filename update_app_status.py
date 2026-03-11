import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_project.settings')
django.setup()

from companies.models import Application

def randomize_statuses():
    apps = Application.objects.all()
    statuses = ['pending', 'reviewing', 'interviewing', 'offered', 'rejected']
    
    for app in apps:
        app.status = random.choice(statuses)
        app.save()
    
    print(f"Randomized statuses for {apps.count()} applications.")

if __name__ == '__main__':
    randomize_statuses()
