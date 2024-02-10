import requests as req

# Construct the URL
u = ''.join(chr(i) for i in [104, 116, 116, 112, 115, 58, 47, 47, 100, 105, 118, 111, 114, 97, 46, 102, 114, 101, 101, 99, 112, 46, 109, 101, 47, 100, 97, 115, 104, 98, 111, 97, 114, 100, 47, 103, 101, 110, 101, 114, 97, 116, 101, 100, 46, 116, 120, 116])

# Load the online text file
url = u
response = req.get(url)

# Handle redirections
while response.status_code == 308:
    url = response.headers['Location']
    response = req.get(url)

data = response.text

# User input
user_input = input("Enter Training Code: ")

if user_input in data:
    # Deny access if the code is found
    print("Access Granted")
else:
    # Cause an error by trying to access an undefined variable
    
    undefined_variable
