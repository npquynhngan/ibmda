"""LOAD THE DATASET"""

# Import the necessary libraries
import pandas

# The dataset is available at the following URL
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

# Load the data into a pandas DataFrame
df = pandas.read_csv(url)

"""EXPLORE THE DATASET"""

# Display the first five rows of the DataFrame
print(df.head())

# Display the number of rows and columns in the DataFrame
print(df.shape)

# Print the number of columns in the DataFrame
print(len(df.columns))

# Identify the data types of the columns in the DataFrame
print(df.dtypes)

# Print the mean age of the survey participants
print(df["Age"].mean())

# Print how many unique countries are there in the DataFrame
print(df["Country"].nunique())

