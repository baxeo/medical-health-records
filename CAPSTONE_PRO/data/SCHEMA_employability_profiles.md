# Youth Employability Profiles Schema

This schema documents the structure of the synthetic youth employability dataset generated for the capstone project.

## Fields

| Field | Type | Description |
|------|------|-------------|
| ProfileID | Integer | Unique identifier for each profile |
| Age | Integer | Age of the youth candidate |
| Gender | String | Gender of the candidate (Male/Female) |
| Region | String | Geographic region in Tanzania |
| EducationLevel | String | Highest completed education level |
| FieldOfStudy | String | Candidate's field of study |
| ExperienceYears | Integer | Total years of work experience |
| YearsSinceGraduation | Integer | Years since graduation |
| DigitalSkillLevel | String | Self-reported digital skills level |
| EnglishLevel | String | Self-reported English skill level |
| CurrentEmploymentStatus | String | Current work situation |
| DesiredIndustry | String | Industry candidate wants to work in |
| PreferredJobType | String | Preferred job setting |
| TechnicalSkills | String | Comma-separated technical skill list |
| SoftSkills | String | Comma-separated soft skill list |
| CertificationsCount | Integer | Number of certifications held |

## Notes
- The generated dataset contains 1000 synthetic records.
- Values are sampled to match the structure and general distribution of the attached sample file.
- The dataset is saved as `data/youth_employability_profiles.csv`.
