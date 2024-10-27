# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv"
df = pd.read_csv(file_path)

"""DISTRIBUTION"""
"""DETERMINE HOW THE DATA IS DISTRIBUTED"""

# The column <ConvertedComp> contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01
# Assuming 12 working months and 50 working weeks
# Plot the distribution of the column <ConvertedComp> from the dataframe <df>

# Using the seaborn library, plot the distribution curve of the column <ConvertedComp>
ax = sns.displot(df['ConvertedComp'], kind='kde')
ax.set(title='Distribution of ConvertedComp', xlabel='ConvertedComp', ylabel='Density')
plt.savefig('converted_comp_dist.png')
plt.close()

# Using the seaborn library, plot the histogram of the column <ConvertedComp>
ax = sns.histplot(df['ConvertedComp'], kde=False)
ax.set(title='Distribution of ConvertedComp', xlabel='ConvertedComp', ylabel='Frequency')
plt.savefig('converted_comp_hist.png')
plt.close()

# What is the median of the column <ConvertedComp>?
median = df['ConvertedComp'].median()
print(f'The median of the column <ConvertedComp> is {median}')

# How many respondents identified themselves only as a Man?
print(df['Gender'].value_counts())

# Find out the median ConvertedComp of respondents identified themselves only as a Woman
print(df[df['Gender'] == 'Woman']['ConvertedComp'].median())

# Find out the median ConvertedComp of respondents identified themselves only as a Man
print(df[df['Gender'] == 'Man']['ConvertedComp'].median())

# Give the five-number summary for the column <Age>
five_number_summary = df['Age'].describe()
print(five_number_summary)

# Plot a histogram of the column <Age>
ax = sns.histplot(df['Age'], kde=False)
ax.set(title='Distribution of Age', xlabel='Age', ylabel='Frequency')
plt.savefig('age_hist.png')
plt.close()

# What is the median of the column <Age>?
median = df['Age'].median()
print(f'The median of the column <Age> is {median}')

"""OUTLIERS"""
"""DETERMINE THE OUTLIERS IN THE DATA"""

# Find out if outliers exist in the column <ConvertedComp> using a box plot
ax = sns.boxplot(x=df['ConvertedComp'])
ax.set(title='Boxplot of ConvertedComp', xlabel='ConvertedComp')
plt.savefig('converted_comp_box.png')
plt.close()

# Find out if outliers exist in the column <Age> using a box plot
ax = sns.boxplot(x=df['Age'])
ax.set(title='Boxplot of Age', xlabel='Age')
plt.savefig('age_box.png')
plt.close()

# Find out the Inter Quartile Range for the column <ConvertedComp>
print(df['ConvertedComp'].quantile(0.75) - df['ConvertedComp'].quantile(0.25))

# Find out the upper and lower bounds for the column <ConvertedComp>
print(f'Lower bound: {df["ConvertedComp"].quantile(0.25) - 1.5 * (df["ConvertedComp"].quantile(0.75) - df["ConvertedComp"].quantile(0.25))}')
print(f'Upper bound: {df["ConvertedComp"].quantile(0.75) + 1.5 * (df["ConvertedComp"].quantile(0.75) - df["ConvertedComp"].quantile(0.25))}')

# Idenitfy how many outliers are there in the column <ConvertedComp>
print(
    len(
        df[
            (df['ConvertedComp'] < df["ConvertedComp"].quantile(0.25) - 1.5 * (df["ConvertedComp"].quantile(0.75) - df["ConvertedComp"].quantile(0.25))) | 
            (df['ConvertedComp'] > df["ConvertedComp"].quantile(0.75) + 1.5 * (df["ConvertedComp"].quantile(0.75) - df["ConvertedComp"].quantile(0.25)))
            ]
        )
    )

# Create a new dataframe by removing the outliers from the column <ConvertedComp>
df_no_outliers = df[
    (
        df['ConvertedComp'] >= df["ConvertedComp"].quantile(0.25) - 1.5 * (df["ConvertedComp"].quantile(0.75) - df["ConvertedComp"].quantile(0.25))
    ) 
    & 
    (
        df['ConvertedComp'] <= df["ConvertedComp"].quantile(0.75) + 1.5 * (df["ConvertedComp"].quantile(0.75) - df["ConvertedComp"].quantile(0.25))
    )
]
print(df_no_outliers.shape)

# Calculate the mean and median of the new dataframe
print(f'Mean: {df_no_outliers['ConvertedComp'].mean()}')
print(f'Median: {df_no_outliers['ConvertedComp'].median()}')

"""CORRELATION"""
"""DETERMINE THE CORRELATION BETWEEN VARIABLES"""

# Find out the correlation between the columns <Age> and all other numerical columns
df_numeric = df.select_dtypes(include='number')
correlation = df_numeric.corr()['Age']
print(correlation)