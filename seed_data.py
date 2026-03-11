import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_project.settings')
django.setup()

from companies.models import Company, Job

def populate_data():
    industries = ['Technology', 'Finance', 'Healthcare', 'E-commerce', 'Education']
    locations = ['San Francisco, CA', 'New York, NY', 'Remote', 'London, UK', 'Austin, TX', 'Bangalore, India']
    
    companies_data = [
        ('TechNova Solutions', 'Technology'),
        ('Global Finance Corp', 'Finance'),
        ('HealthFirst Systems', 'Healthcare'),
        ('EcoShop Intl', 'E-commerce'),
        ('EduSmart Platform', 'Education'),
        ('CloudScale Systems', 'Technology'),
        ('FinEdge Analytics', 'Finance'),
        ('BioCare Researh', 'Healthcare'),
        ('ShopSwift', 'E-commerce'),
        ('LearnAnywhere', 'Education'),
        ('CyberShield AI', 'Technology'),
        ('PeakWealth Management', 'Finance'),
        ('MedConnect', 'Healthcare'),
        ('MarketFlow', 'E-commerce'),
        ('SkillUp University', 'Education'),
    ]

    skills_pool = ['Python', 'Django', 'React', 'JavaScript', 'SQL', 'AWS', 'Docker', 'Kubernetes', 'Java', 'C++', 'Project Management', 'Data Analysis']

    for name, industry in companies_data:
        company, created = Company.objects.get_or_create(
            name=name,
            defaults={
                'industry': industry,
                'location': random.choice(locations),
                'description': f"A leading company in the {industry} sector focusing on innovation."
            }
        )

        # Create 1-2 jobs for each company
        for i in range(random.randint(1, 2)):
            job_skills = random.sample(skills_pool, random.randint(3, 5))
            Job.objects.create(
                company=company,
                title=f"Senior {random.choice(skills_pool)} Developer" if random.choice([True, False]) else f"{industry} Specialist",
                required_skills=", ".join(job_skills),
                required_experience=random.randint(1, 10),
                salary_range=f"${random.randint(50, 150)}k - ${random.randint(160, 250)}k",
                location=random.choice(locations),
                description="We are looking for a motivated individual to join our growing team."
            )

    print("Demo data populated successfully!")

if __name__ == '__main__':
    populate_data()
