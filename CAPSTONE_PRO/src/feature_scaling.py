"""
Feature Scaling using StandardScaler
Prepares numeric features for clustering.
"""
import json
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

INPUT_PATH = 'data/youth_profiles_encoded.csv'
OUTPUT_PATH = 'data/youth_profiles_scaled.csv'
SCALER_PATH = 'data/standard_scaler.pkl'

# Features to scale (exclude ProfileID which is just an identifier)
FEATURES_TO_SCALE = [
    'Age',
    'ExperienceYears',
    'YearsSinceGraduation',
    'YearsGap',
    'DigitalSkillEncoded',
    'EnglishLevelEncoded',
    'TechSkillCount',
    'SoftSkillCount',
    'CertificationsCount'
]

# Encoded features (already numeric, will be scaled)
ENCODED_FEATURES = [
    'GenderEncoded',
    'RegionEncoded',
    'EducationEncoded',
    'FieldOfStudyEncoded',
    'CurrentEmploymentStatusEncoded',
    'DesiredIndustryEncoded',
    'PreferredJobTypeEncoded',
    'HasPythonSkill',
    'HasDigitalMarketing'
]

ALL_SCALING_FEATURES = FEATURES_TO_SCALE + ENCODED_FEATURES


def main():
    # Load encoded data
    df = pd.read_csv(INPUT_PATH)
    
    # Initialize scaler
    scaler = StandardScaler()
    
    # Fit and transform scaling features
    df_scaled = df.copy()
    df_scaled[ALL_SCALING_FEATURES] = scaler.fit_transform(df[ALL_SCALING_FEATURES])
    
    # Save scaled dataset
    df_scaled.to_csv(OUTPUT_PATH, index=False)
    
    # Save scaler for later use
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
    
    print('✓ Feature Scaling Complete')
    print(f'  Input: {INPUT_PATH}')
    print(f'  Output: {OUTPUT_PATH}')
    print(f'  Scaler saved: {SCALER_PATH}')
    print(f'\n  Scaled features ({len(ALL_SCALING_FEATURES)}):')
    for feat in ALL_SCALING_FEATURES:
        print(f'    - {feat}')
    print(f'\n  Unscaled features:')
    print(f'    - ProfileID (identifier)')
    
    # Print statistics
    print(f'\n  Scaling Statistics:')
    print(f'    Mean (all features): {df_scaled[ALL_SCALING_FEATURES].mean().mean():.6f}')
    print(f'    Std (all features): {df_scaled[ALL_SCALING_FEATURES].std().mean():.6f}')
    print(f'\n  Sample scaled values (first 5 rows):')
    print(df_scaled[['ProfileID', 'Age', 'ExperienceYears', 'TechSkillCount']].head().to_string(index=False))


if __name__ == '__main__':
    main()
