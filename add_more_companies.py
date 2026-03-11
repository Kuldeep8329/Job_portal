import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_project.settings')
django.setup()

from companies.models import Company, Job

def add_more_data():
    industries = ['Technology', 'Finance', 'Healthcare', 'E-commerce', 'Education']
    locations = ['Seattle, WA', 'Chicago, IL', 'Remote', 'Berlin, Germany', 'Toronto, Canada', 'Sydney, Australia', 'Tokyo, Japan']
    
    new_companies = [
        ('Quantum Leap Labs', 'Technology'),
        ('Silver Capital', 'Finance'),
        ('Vitality Health', 'Healthcare'),
        ('Z-Commerce', 'E-commerce'),
        ('Future Minds Academy', 'Education'),
        ('Orbit SpaceTech', 'Technology'),
        ('Prime Asset Group', 'Finance'),
        ('WellNest Clinics', 'Healthcare'),
        ('QuickCart', 'E-commerce'),
        ('BrainBridge Learning', 'Education'),
        ('DeepCode AI', 'Technology'),
        ('Horizon Wealth', 'Finance'),
        ('Pulse Point Med', 'Healthcare'),
        ('SwiftShip Direct', 'E-commerce'),
        ('Elite Scholar Hub', 'Education'),
    ]

    skills_pool = ['Python', 'Django', 'React', 'JavaScript', 'SQL', 'AWS', 'Docker', 'Kubernetes', 'Java', 'C++', 'Project Management', 'Data Analysis', 'Swift', 'Kotlin', 'Rust', 'Go', 'Figma', 'Node.js']

    for name, industry in new_companies:
        company, created = Company.objects.get_or_create(
            name=name,
            defaults={
                'industry': industry,
                'location': random.choice(locations),
                'description': f"An industry leader in {industry} dedicated to excellence and forward-thinking solutions."
            }
        )

        if created:
            # Create 1-3 jobs for each new company
            for i in range(random.randint(1, 3)):
                job_skills = random.sample(skills_pool, random.randint(3, 6))
                role_type = random.choice(['Lead', 'Senior', 'Junior', 'Staff', 'Principal', ''])
                title = f"{role_type} {random.choice(skills_pool)} Engineer".strip() if random.choice([True, False]) else f"{industry} Consultant"
                
                Job.objects.create(
                    company=company,
                    title=title,
                    required_skills=", ".join(job_skills),
                    required_experience=random.randint(1, 12),
                    salary_range=f"${random.randint(70, 180)}k - ${random.randint(190, 300)}k",
                    location=random.choice(locations),
                    description="We are expanding our team and looking for world-class talent to help us build the future."
                )

    print("15 Additional demo companies and their jobs added successfully!")

if __name__ == '__main__':
    add_more_data()
