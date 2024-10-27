"""EXTRACT INFORMATION FROM THE GIVEN WEBSITE"""

# Importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
# The data you need to scrape is the name of the programming language and average annual salary
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

# Download the webpage at the URL
data = requests.get(url).text

# Create a soup object
soup = BeautifulSoup(data, "html.parser")

# Scrape the language name and annual average salary
# Create a list to store the data
language_data = []

# Get the table
table = soup.find('table')

# Get all rows from the table
for idx, row in enumerate(table.find_all('tr')):
    if idx == 0: # skip the header row
        continue
    cols = row.find_all('td')
    language_name = cols[1].getText()
    avg_salary = cols[3].getText()
    language_data.append([language_name, avg_salary])

# Create a DataFrame
df = pd.DataFrame(language_data, columns=['Language', 'Average Annual Salary'])

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('popular-languages.csv', index=False)