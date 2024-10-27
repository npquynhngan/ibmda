"""SCARPE WWW.IBM.COM"""

# Import the required modules and functions
import requests # this module helps us to download a web page
from bs4 import BeautifulSoup # this module helps in web scrapping
import pandas as pd

# Download the content of the web page
url = "http://www.ibm.com"

# get the contents of the web page in text format and store in a variable called data
data  = requests.get(url).text

# Create a soup object
soup = BeautifulSoup(data,"html.parser")

# Scrape all links
for link in soup.find_all('a'): # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

# Scrape all images
for img in soup.find_all('img'): # in html image is represented by the tag <img>
    print(img.get('src'))

"""SCRAPE DATA FROM HTML TABLES"""

# The below URL contains an HTML table with data about colors and color codes
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# Get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

# Create a soup object
soup = BeautifulSoup(data,"html.parser")

# Find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

# Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].getText() # store the value in column 3 as color_name
    color_code = cols[3].getText() # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

