import urllib.request
import sys

# Load the online text file
url = "https://user-final.shilohpendergra.repl.co/dashboard/generated.txt"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

# User input
user_input = input("Enter Training Code: ")

if user_input in data:
    print("Access granted")
else:
    print("Access denied")
    sys.exit(1)  # Exiting with a non-zero status to indicate an error
