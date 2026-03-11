import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_project.settings')
django.setup()

from companies.models import Company, Job

def update_to_it_sector():
    # Update all companies to Technology industry
    companies_updated = Company.objects.all().update(industry='Technology')
    
    # Update job titles to be IT-focused if they aren't already
    # For simplicity, we just ensure the industry is Technology for all companies, 
    # as the user requested "all 30 jobs as IT sector jobs".
    # Most existing jobs in the script I wrote previously were already IT focused.
    
    # Let's check for any non-IT titles and refine them
    non_it_keywords = ['Wealth', 'Clinic', 'Scholar', 'Asset', 'Consign']
    it_titles = [
        'Full Stack Developer', 'Cloud Architect', 'DevOps Engineer', 
        'Data Scientist', 'Cybersecurity Specialist', 'Frontend Engineer',
        'Backend Developer', 'IT Consultant', 'Mobile App Developer',
        'System Administrator', 'Network Engineer', 'QA Engineer'
    ]
    
    jobs = Job.objects.all()
    jobs_updated_count = 0
    for job in jobs:
        needs_update = False
        for kw in non_it_keywords:
            if kw.lower() in job.title.lower():
                needs_update = True
                break
        
        if needs_update:
            job.title = f"Senior {it_titles[jobs_updated_count % len(it_titles)]}"
            job.save()
            jobs_updated_count += 1

    print(f"Updated {companies_updated} companies to the Technology industry.")
    print(f"Refined {jobs_updated_count} job titles to be IT-specific.")

if __name__ == '__main__':
    update_to_it_sector()
