import requests

# Load the online text file
url = "https://user-final.shilohpendergra.repl.co/dashboard/generated.txt"
response = requests.get(url)

# Handle redirections
while response.status_code == 308:
    url = response.headers['Location']
    response = requests.get(url)

data = response.text

# User input
user_input = input("Enter Training Code: ")

if user_input in data:
    print("Access granted")
else:
    print("Access denied")
