# Import the library
import requests
import io
from PIL import Image

# Define the URL
url_text = 'https://www.ibm.com/'

# Send the GET request
response = requests.get(url_text)

# Print the status code
print(response.status_code)

# Print the request headers
print(response.request.headers)

# Print the request body
print("request body:", response.request.body)

# Print the response headers
print("response headers:", response.headers)

# Print the date the request was sent
print(response.headers['date'])

# Print the content type of the response
print(response.headers['Content-Type'])

# Print the encoding of the response
print(response.encoding)

# As the Content-Type is text/html, we can use the attribute text to display the HTML in the body
# We can use the method text to display the first 100 characters:
print(response.text[0:100])

# Load oher types of data for non-text requests
url_image = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

# Send the GET request
response = requests.get(url_image)

# Print the response header
print(response.headers)

# Check the content type
print(response.headers['Content-Type'])

# An image is a response object that contains the image as a byte array
# We must save it to a file
# Define the file name
file_name = 'image.png'

# Save the image
# Open the file in write binary mode
# Use the attribute content to return the image as a byte array
with open(file_name, 'wb') as file:
    file.write(response.content)

# Open the image file
image = Image.open(file_name)

"""QUESTION: DOWNLOAD A FILE"""

# Define the URL
url_1 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

# Send the GET request
response = requests.get(url_1)

# Download the file
with open('Example1.txt', 'wb') as file:
    file.write(response.content)

# Open the file
with open('Example1.txt', 'r') as file:
    print(file.read())