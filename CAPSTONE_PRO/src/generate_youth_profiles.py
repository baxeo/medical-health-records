"""
Synthetic Youth Employability Profile Data Generator
Generates 1000 records matching the attached youth employability dataset schema.
"""
import csv
import random

# Seed for reproducibility
random.seed(42)

REGIONS = [
    'Arusha', 'Dar es Salaam', 'Dodoma', 'Geita', 'Iringa', 'Kagera', 'Kigoma',
    'Kilimanjaro', 'Lindi', 'Manyara', 'Mara', 'Mbeya', 'Morogoro', 'Mtwara',
    'Mwanza', 'Njombe', 'Pwani', 'Rukwa', 'Ruvuma', 'Shinyanga', 'Simiyu',
    'Singida', 'Tabora', 'Tanga', 'Katavi', 'Zanzibar Urban/West', 'Zanzibar South',
    'Songwe', 'Pemba North', 'Pemba South'
]

GENDERS = ['Male', 'Female']
EDUCATION_LEVELS = [
    'Higher Diploma', 'Vocational/Technical', 'Secondary',
    'No formal qualification', 'Diploma', 'Bachelor'
]
FIELDS_OF_STUDY = [
    'Logistics', 'Agriculture', 'Engineering', 'Arts', 'Finance',
    'Information Technology', 'Education', 'Health', 'Business', 'Hospitality'
]
DIGITAL_SKILL_LEVEL = ['High', 'Medium', 'Low']
ENGLISH_LEVEL = ['Basic', 'Intermediate', 'Advanced']
EMPLOYMENT_STATUS = [
    'Self-employed', 'Unemployed', 'Part-time', 'Full-time', 'Internship', 'Informal work'
]
DESIRED_INDUSTRY = [
    'Trade', 'Manufacturing', 'Agriculture', 'Education', 'Construction',
    'Banking', 'Tourism', 'Healthcare', 'Transport', 'ICT'
]
PREFERRED_JOB_TYPE = ['Remote', 'Field', 'Customer-facing', 'Office']
TECHNICAL_SKILLS = [
    'Data analysis', 'Programming (Python)', 'Digital marketing', 'Sales',
    'Microsoft Office', 'Mechanical maintenance', 'Graphic design',
    'Customer service', 'Project management', 'English communication',
    'Accounting', 'Database management', 'Network support',
    'Social media management', 'Web development', 'Quality control',
    'Inventory management', 'Logistics coordination', 'Food preparation', 'Teaching support'
]
SOFT_SKILLS = [
    'Communication', 'Problem solving', 'Teamwork', 'Adaptability',
    'Time management', 'Creativity', 'Critical thinking', 'Resilience',
    'Leadership', 'Customer focus'
]

CSV_HEADERS = [
    'ProfileID', 'Age', 'Gender', 'Region', 'EducationLevel', 'FieldOfStudy',
    'ExperienceYears', 'YearsSinceGraduation', 'DigitalSkillLevel', 'EnglishLevel',
    'CurrentEmploymentStatus', 'DesiredIndustry', 'PreferredJobType',
    'TechnicalSkills', 'SoftSkills', 'CertificationsCount'
]


def generate_age():
    # Most records are between 18 and 29, centered around 23
    age = int(random.gauss(23.5, 2.8))
    return min(max(age, 18), 29)


def generate_years_since_graduation(age):
    # Graduation occurs approx age 17-23, with small gap for youngest individuals
    max_years = min(age - 17, 9)
    if max_years < 0:
        return 0
    value = random.choice(range(max_years + 1))
    return value


def generate_experience_years(years_since_grad):
    # Experience is usually not greater than years since graduation
    exp = random.choice(range(years_since_grad + 1))
    if exp > 8:
        exp = 8
    return exp


def choose_skills(pool, min_count=2, max_count=5):
    count = random.randint(min_count, max_count)
    return ', '.join(random.sample(pool, count))


def generate_record(record_id):
    age = generate_age()
    education = random.choices(
        EDUCATION_LEVELS,
        weights=[20, 18, 18, 10, 16, 18],
        k=1
    )[0]
    years_since_grad = generate_years_since_graduation(age)
    experience = generate_experience_years(years_since_grad)
    digital_skill = random.choices(DIGITAL_SKILL_LEVEL, weights=[30, 45, 25], k=1)[0]
    english = random.choices(ENGLISH_LEVEL, weights=[35, 45, 20], k=1)[0]
    status = random.choices(EMPLOYMENT_STATUS, weights=[18, 20, 14, 18, 12, 18], k=1)[0]
    desired = random.choice(DESIRED_INDUSTRY)
    preferred = random.choice(PREFERRED_JOB_TYPE)
    technical = choose_skills(TECHNICAL_SKILLS, min_count=2, max_count=4)
    soft = choose_skills(SOFT_SKILLS, min_count=2, max_count=3)
    cert_count = random.choices([0, 1, 2, 3], weights=[18, 42, 28, 12], k=1)[0]

    return [
        record_id,
        age,
        random.choice(GENDERS),
        random.choice(REGIONS),
        education,
        random.choice(FIELDS_OF_STUDY),
        experience,
        years_since_grad,
        digital_skill,
        english,
        status,
        desired,
        preferred,
        technical,
        soft,
        cert_count
    ]


def save_data(filepath='data/youth_employability_profiles.csv', n_records=1000):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(CSV_HEADERS)
        for profile_id in range(1, n_records + 1):
            writer.writerow(generate_record(profile_id))
    print(f'✓ Synthetic dataset generated: {filepath}')
    print(f'  Records: {n_records}')


if __name__ == '__main__':
    save_data()