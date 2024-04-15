import requests as req

# Construct the URL
url = 'https://divoratech.com/dashboard/generate.tzt'

# Load the online text file
response = req.get(url)

# Handle redirections
while response.status_code == 308:
    url = response.headers['Location']
    response = req.get(url)

data = response.text

# User input
user_input = input("Enter Training Code: ")

if user_input in data:
    # Grant access if the code is found
    print("Access Granted")
else:
    # Cause an error by trying to access an undefined variable
    undefined_variable
