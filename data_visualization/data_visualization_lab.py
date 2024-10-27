"""DATABASE"""

# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import requests

# URL of the file you want to download
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite'
# Download the file and save it to the current directory
response = requests.get(url)
with open('m4_survey_data.sqlite', 'wb') as file:
    file.write(response.content)
print("Download complete.")

# Connecting to the database
conn = sqlite3.connect('m4_survey_data.sqlite')

# Run a query to find out the number of rows in the table named 'master'
query = "SELECT COUNT(*) FROM master"
# Print the result of the query
print(pd.read_sql_query(query, conn))

# Run a query to list all tables
query = "SELECT name FROM sqlite_master WHERE type='table'"
# Print the result of the query
print(pd.read_sql_query(query, conn))

# Run a query to describe the table named 'master'
query = "PRAGMA table_info(master)"
# Print the result of the query
print(pd.read_sql_query(query, conn))

# Read the data from the database and store it in a dataframe
df = pd.read_sql_query("SELECT * FROM master", conn)
# Display the first five rows of the dataframe
print(df.head())
print(df.columns)

"""DATA VISUALIZATION"""
"""VISUALIZING DISTRIBUTION OF DATA"""

# Plot a histogram of <ConvertedComp> column
ax = sns.histplot(df['ConvertedComp'], bins=10, kde=True)
ax.set_title('Distribution of ConvertedComp')
ax.set_xlabel('ConvertedComp')
ax.set_ylabel('Frequency')
plt.savefig('histogram.png')
plt.close()

# Plot a boxplot of <Age> column
ax = sns.boxplot(x=df['Age'])
ax.set_title('Boxplot of Age')
plt.savefig('boxplot.png')
plt.close()

"""VISUALIZING RELATIONSHIPS IN DATA"""

# Plot a scatter plot of <Age> and <WorkWeekHrs> columns
ax = sns.scatterplot(x='Age', y='WorkWeekHrs', data=df)
ax.set_title('Scatter plot of Age and WorkWeekHrs')
ax.set_xlabel('Age')
ax.set_ylabel('WorkWeekHrs')
plt.savefig('scatterplot.png')
plt.close()

# Plot a bubble plot of WorkWeekHrs and CodeRevHrs columns, use Age column as bubble size
ax = sns.scatterplot(x='WorkWeekHrs', y='CodeRevHrs', size='Age', data=df, legend="brief")
ax.set_title('Bubble plot of WorkWeekHrs and CodeRevHrs')
ax.set_xlabel('WorkWeekHrs')
ax.set_ylabel('CodeRevHrs')
plt.savefig('bubbleplot.png')
plt.close()

"""VISUALIZING COMPOSITION OF DATA"""

# Run a query to load the data from the table 'DatabaseDesireNextYear' and store it in a dataframe
df_db = pd.read_sql_query("SELECT * FROM DatabaseDesireNextYear", conn)
print(df_db.columns)

# Plot a pie chart of the top 5 databases that respondents wish to learn next year
# Label the pie chart with the names of the databases
# Display the percentages on the pie chart
df_db = df_db['DatabaseDesireNextYear'].value_counts().head()
ax = df_db.plot.pie(autopct='%1.1f%%', startangle=90, labels=df_db.index)
plt.title('Top 5 Databases Desired to Learn Next Year')
plt.savefig('piechart.png')
plt.close()

# Run a query to load the data from the table 'LanguageDesireNextYear' and store it in a dataframe
df_lang = pd.read_sql_query("SELECT * FROM LanguageDesireNextYear", conn)
print(df_lang.columns)

# Plot a bar chart of the top 5 languages that respondents wish to learn next year
# The x-axis should have the names of the languages
# The y-axis should have the number of respondents
df_lang = df_lang['LanguageDesireNextYear'].value_counts().head()
ax = df_lang.plot.bar()
ax.set_title('Top 5 Languages Desired to Learn Next Year')
ax.set_xlabel('Languages')
ax.set_ylabel('Number of Respondents')
plt.savefig('barchart.png')
plt.close()

# Run a query to load the data from the table 'LanguageWorkedWith' and store it in a dataframe
df_lang_worked = pd.read_sql_query("SELECT * FROM LanguageWorkedWith", conn)
print(df_lang_worked.columns)

# Find out the number of respondents who worked with SQL
sql_count = df_lang_worked['LanguageWorkedWith'].str.contains('SQL').sum()
print(f'Number of respondents who worked with SQL: {sql_count}')

# Run a query to load the data from the table 'DatabaseWorkedWith' and store it in a dataframe
df_db_worked = pd.read_sql_query("SELECT * FROM DatabaseWorkedWith", conn)
print(df_db_worked.columns)
print(df_db_worked['DatabaseWorkedWith'].value_counts())

# Find out the number of respondents who worked with MySQL only
mysql_count = df_db_worked[df_db_worked['DatabaseWorkedWith'] == 'MySQL'].sum()
print(f'Number of respondents who worked with MySQL only: {mysql_count}')

# Run a query to load the data from the table 'DevType' and store it in a dataframe
df_dev = pd.read_sql_query("SELECT * FROM DevType", conn)
print(df_dev.columns)

# Find out the majority developer type of the respondents
dev_count = df_dev['DevType'].value_counts().idxmax()
print(f'Majority developer type: {dev_count}')

# Plot a stacked bar chart of median WorkWeekHrs and CodeRevHrs for the age group 30 to 35
# The x-axis should have two bars for each age group
# The y-axis should have the median WorkWeekHrs and CodeRevHrs
df_age = df[(df['Age'] >= 30) & (df['Age'] <= 35)].groupby('Age')[['WorkWeekHrs', 'CodeRevHrs']].median()
ax = df_age.plot.bar(stacked=True)
ax.set_title('Median WorkWeekHrs and CodeRevHrs for Age Group 30-35')
ax.set_xlabel('Age')
ax.set_ylabel('Median Hours')
plt.savefig('stackedbarchart.png')
plt.close()

"""VISUALIZING COMPARISONS IN DATA"""

# Plot a line chart of median ConvertedComp for the age group 45 to 60
# The x-axis should have the age
# The y-axis should have the median ConvertedComp
df_age = df[(df['Age'] >= 45) & (df['Age'] <= 60)].groupby('Age')['ConvertedComp'].median()
ax = df_age.plot.line()
ax.set_title('Median ConvertedComp for Age Group 45-60')
ax.set_xlabel('Age')
ax.set_ylabel('Median ConvertedComp')
plt.savefig('linechart.png')
plt.close()

# Plot a line chart of median ConvertedComp for the age group 25 to 30
# The x-axis should have the age
# The y-axis should have the median ConvertedComp
df_age = df[(df['Age'] >= 25) & (df['Age'] <= 30)].groupby('Age')['ConvertedComp'].median()
ax = df_age.plot.line()
ax.set_title('Median ConvertedComp for Age Group 25-30')
ax.set_xlabel('Age')
ax.set_ylabel('Median ConvertedComp')
plt.savefig('linechart2.png')
plt.close()

# Plot a horizontal bar chart using the column <MainBranch>
# The y-axis should have the MainBranch
# The x-axis should have the median ConvertedComp
df_mainbranch = df.groupby('MainBranch')['ConvertedComp'].median().sort_values()
ax = df_mainbranch.plot.barh()
ax.set_title('Median ConvertedComp by MainBranch')
ax.set_xlabel('Median ConvertedComp')
ax.set_ylabel('MainBranch')
plt.savefig('horizontalbarchart.png')
plt.close()

# Close the connection
conn.close()