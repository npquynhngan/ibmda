# Import libraries
import requests
import json
import io
import pandas as pd

"""WARM UP EXERCISES"""
"""FIND OUT WHO IS IN SPACE RIGHT NOW"""

# Define the API endpoint
url = "http://api.open-notify.org/astros.json"

# Make a GET request to the API
response = requests.get(url)

if response.ok: # if all is well (e.g. no errors, no network timeouts)
    # Parse the JSON data
    data = response.json() # the variable is of type dictionary
    # Print the JSON data
    print(data)

# Extract the number of astronauts
number_of_astronauts = data['number']
print(f"Number of astronauts in space: {number_of_astronauts}")

# Extract the names of astronauts currently on ISS
astronauts = data['people']
print("There are {} astronauts on ISS".format(len(astronauts)))
print("Their names are:")
for astronaut in astronauts:
    print(astronaut['name'])

"""LAB: COLLECT JOBS DATA USING GITHUB JOBS API"""
"""DEFINE THE NUMBER OF JOBS CURRENTLY OPEN FOR VARIOUS TECHNOLOGIES AND FOR VARIOUS LOCATIONS"""

# Define the API endpoint
url = 'http://127.0.0.1:5000/data'

# Write a function to get the number of jobs for the Python technologies
def get_number_of_jobs(technology):
    # Make a GET request to the API
    payload = {'Key Skills': technology}
    response = requests.get(url, params=payload)
    if response.ok: # if all is well (e.g. no errors, no network timeouts)
        # Parse the JSON data
        data = response.json()
        # Extract the number of jobs for the technology
        number_of_jobs = len(data)
        return technology, number_of_jobs
    else:
        return None
    
# Calling the function for Python and check if it works
technology = 'Python'
technology, number_of_jobs = get_number_of_jobs(technology)
print(f"Number of jobs for {technology}: {number_of_jobs}")

"""WRITE A FUNCTION TO FIND THE NUMBER OF JOBS IN US FOR A LOCATION OF YOUR CHOICE"""
"""LOS ANGELES"""

# Write a function to get the number of jobs in US for a location of your choice
def get_number_of_jobs_in_us(location):
    # Make a GET request to the API
    payload = {'Location': location}
    response = requests.get(url, params=payload)
    if response.ok: # if all is well (e.g. no errors, no network timeouts)
        # Parse the JSON data
        data = response.json()
        # Extract the number of jobs for the location
        number_of_jobs = len(data)
        return location, number_of_jobs
    else:
        return None
    
# Calling the function for Los Angeles and check if it works
location = 'Los Angeles'
location, number_of_jobs = get_number_of_jobs_in_us(location)
print(f"Number of jobs in US for {location}: {number_of_jobs}")

"""STORE THE RESULTS IN AN EXCEL FILE"""
from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "github-job-postings-technology"
ws.append(["Technology", "Number of Jobs"])

# Create a Python list of technologies
technologies = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB']

# Write the number of jobs for each technology to the Excel file
for technology in technologies:
    technology, number_of_jobs = get_number_of_jobs(technology)
    ws.append([technology, number_of_jobs])

# Save the Excel workbook
wb.save("github-job-postings-technology.xlsx")

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "github-job-postings-location"
ws.append(["Location", "Number of Jobs"])

# Create a Python list of locations
locations = ['Los Angeles', 'New York', 'San Francisco', 'Washington DC', 'Seattle', 'Austin', 'Detroit']

# Write the number of jobs for each location to the Excel file
for location in locations:
    location, number_of_jobs = get_number_of_jobs_in_us(location)
    ws.append([location, number_of_jobs])

# Save the Excel workbook
wb.save("github-job-postings-location.xlsx")