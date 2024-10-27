# Import libraries
import requests

"""GET Request"""

# Define the URL
url_get='http://httpbin.org/get'

# Create a dictionary
payload={"name":"Joseph","ID":"123"}

# Pass the dictionary to the params parameter of the get() function
r=requests.get(url_get,params=payload)

# Print the URL and see the name and ID parameters in the URL
print(r.url)

# Print the status code
print(r.status_code)

# Print the response text
print(r.text)

# Print the Content-Type
print(r.headers['Content-Type'])

# As the Content-Type is in JSON format we can use the method json() to display the JSON in the body
# It returns a dictionary
print(r.json())

# The key args contains the name and ID
print(r.json()['args'])


"""POST Request"""

# Define the URL
post_url = 'https://httpbin.org/post'

# Define the payload
payload={"name":"Joseph","ID":"123"}

# Pass the dictionary to the data parameter of the post() function
r_post = requests.post(post_url, data=payload)

# Comparing the URL from the GET and POST request
print("GET request URL:", r.url)
print("POST request URL:", r_post.url)

# Compare the request body from the GET and POST request
print("GET request body:", r.request.body)
print("POST request body:", r_post.request.body)

# Print the form
print(r_post.json()['form'])