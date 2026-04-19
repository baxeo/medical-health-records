"""
Preprocessing and encoding for youth employability clustering.
Generates a numeric dataset ready for clustering.
"""
import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

INPUT_PATH = 'data/youth_employability_profiles.csv'
OUTPUT_PATH = 'data/youth_profiles_encoded.csv'
MAPPING_PATH = 'data/encoding_mappings.json'

EDUCATION_MAPPING = {
    'No formal qualification': 0,
    'Secondary': 1,
    'Vocational/Technical': 2,
    'Diploma': 3,
    'Higher Diploma': 4,
    'Bachelor': 5
}

DIGITAL_SKILL_MAPPING = {'Low': 0, 'Medium': 1, 'High': 2}
ENGLISH_LEVEL_MAPPING = {'Basic': 0, 'Intermediate': 1, 'Advanced': 2}
GENDER_MAPPING = {'Male': 0, 'Female': 1}

def build_label_encoding(df, column):
    le = LabelEncoder()
    encoded = le.fit_transform(df[column].astype(str))
    return encoded, {label: int(code) for label, code in zip(le.classes_, range(len(le.classes_)))}


def split_skill_text(text):
    if pd.isna(text) or text == '':
        return []
    return [skill.strip() for skill in text.split(',') if skill.strip()]


def main():
    df = pd.read_csv(INPUT_PATH)

    df['GenderEncoded'] = df['Gender'].map(GENDER_MAPPING)
    df['EducationEncoded'] = df['EducationLevel'].map(EDUCATION_MAPPING)
    df['DigitalSkillEncoded'] = df['DigitalSkillLevel'].map(DIGITAL_SKILL_MAPPING)
    df['EnglishLevelEncoded'] = df['EnglishLevel'].map(ENGLISH_LEVEL_MAPPING)

    df['TechSkillCount'] = df['TechnicalSkills'].apply(lambda x: len(split_skill_text(x)))
    df['SoftSkillCount'] = df['SoftSkills'].apply(lambda x: len(split_skill_text(x)))
    df['HasPythonSkill'] = df['TechnicalSkills'].str.contains('Python', case=False, na=False).astype(int)
    df['HasDigitalMarketing'] = df['TechnicalSkills'].str.contains('Digital marketing', case=False, na=False).astype(int)
    df['YearsGap'] = df['YearsSinceGraduation'] - df['ExperienceYears']

    df['RegionEncoded'], region_map = build_label_encoding(df, 'Region')
    df['FieldOfStudyEncoded'], field_map = build_label_encoding(df, 'FieldOfStudy')
    df['CurrentEmploymentStatusEncoded'], status_map = build_label_encoding(df, 'CurrentEmploymentStatus')
    df['DesiredIndustryEncoded'], industry_map = build_label_encoding(df, 'DesiredIndustry')
    df['PreferredJobTypeEncoded'], job_type_map = build_label_encoding(df, 'PreferredJobType')

    encoded_columns = [
        'ProfileID',
        'Age',
        'GenderEncoded',
        'RegionEncoded',
        'EducationEncoded',
        'FieldOfStudyEncoded',
        'ExperienceYears',
        'YearsSinceGraduation',
        'YearsGap',
        'DigitalSkillEncoded',
        'EnglishLevelEncoded',
        'CurrentEmploymentStatusEncoded',
        'DesiredIndustryEncoded',
        'PreferredJobTypeEncoded',
        'TechSkillCount',
        'SoftSkillCount',
        'HasPythonSkill',
        'HasDigitalMarketing',
        'CertificationsCount'
    ]

    df_encoded = df[encoded_columns]
    df_encoded.to_csv(OUTPUT_PATH, index=False)

    mappings = {
        'Gender': GENDER_MAPPING,
        'EducationLevel': EDUCATION_MAPPING,
        'DigitalSkillLevel': DIGITAL_SKILL_MAPPING,
        'EnglishLevel': ENGLISH_LEVEL_MAPPING,
        'Region': region_map,
        'FieldOfStudy': field_map,
        'CurrentEmploymentStatus': status_map,
        'DesiredIndustry': industry_map,
        'PreferredJobType': job_type_map
    }

    with open(MAPPING_PATH, 'w', encoding='utf-8') as f:
        json.dump(mappings, f, indent=2)

    print('✓ Encoding complete')
    print(f'  Input: {INPUT_PATH}')
    print(f'  Output: {OUTPUT_PATH}')
    print(f'  Mappings: {MAPPING_PATH}')
    print('  Encoded columns:')
    for col in encoded_columns:
        print(f'    - {col}')


if __name__ == '__main__':
    main()
