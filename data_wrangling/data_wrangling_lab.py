# Import pandas
import pandas as pd

"""READ DATA"""

# Load the data into a DataFrame
file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

df = pd.read_csv(file_path)

"""DUPLICATES"""
# Finding duplicates
print(df.duplicated().sum())

# Removing duplicates
df = df.drop_duplicates()

# Verify if duplicates were removed
print(df.duplicated().sum())
print(df.shape)

"""MISSING VALUES"""
# Find missing values
missing_values = df.isnull()
print(missing_values.sum())

# Find missing values in column WorkLoc
missing_values_WorkLoc = df['WorkLoc'].isnull().sum()
print(missing_values_WorkLoc)

# Find missing values in volumn EdLevel
missing_values_EdLevel = df['EdLevel'].isnull().sum()
print(missing_values_EdLevel)

# Find missing values in column Country
missing_values_Country = df['Country'].isnull().sum()
print(missing_values_Country)

"""IMPUTE MISSING VALUES"""

# Find the value counts of the column WorkLoc
WorkLoc_counts = df['WorkLoc'].value_counts()

# Identify the most common value in the column WorkLoc
WorkLoc_most_common_value = df['WorkLoc'].value_counts().idxmax()

# Identify the most common value in the column Employment
Employment_most_common_value = df['Employment'].value_counts().idxmax()
print(Employment_most_common_value)

# Idenitfy the most least value in the column UndergradMajor
UndergradMajor_least_common_value = df['UndergradMajor'].value_counts().idxmin()
print(UndergradMajor_least_common_value)

# Impute missing values in column WorkLoc with the most common value
df['WorkLoc'] = df['WorkLoc'].fillna(WorkLoc_most_common_value)

# Verify if missing values were imputed
missing_values_WorkLoc_imputed = df['WorkLoc'].isnull()
print(missing_values_WorkLoc_imputed.sum())

"""NORMALIZATION"""

# Columns "CompFreq" and "CompTotal" have different scales
# Create a new column "NormalizedAnnualCompensation" which contains the "Annual Compensation" irrespective of the "CompFreq"

# List out the various unique values in the column "CompFreq"
CompFreq_unique_values = df['CompFreq'].unique()
print(CompFreq_unique_values)

# Find the value counts of the column "CompFreq" of each of the unique values
compfreq_value_counts = df['CompFreq'].value_counts()
print(compfreq_value_counts)

# Create a new column named "NormalizedAnnualCompensation"
# If the "CompFreq" is "Yearly", copy the value from "CompTotal" to "NormalizedAnnualCompensation"
# If the "CompFreq" is "Monthly", multiply the value in "CompTotal" by 12 and copy it to "NormalizedAnnualCompensation"
# If the "CompFreq" is "Weekly", multiply the value in "CompTotal" by 52 and copy it to "NormalizedAnnualCompensation"
df['NormalizedAnnualCompensation'] = df.apply(
    lambda x: x['CompTotal'] if x['CompFreq'] == 'Yearly' else 
              x['CompTotal'] * 12 if x['CompFreq'] == 'Monthly' else 
              x['CompTotal'] * 52 if x['CompFreq'] == 'Weekly' else 0,
    axis=1
)

# Find the median of the new column "NormalizedAnnualCompensation"
median_NormalizedAnnualCompensation = df['NormalizedAnnualCompensation'].median()
print(median_NormalizedAnnualCompensation)

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_survey_data.csv', index=False)