import urllib.request
from urllib.error import HTTPError

# Load the online text file
url = "https://divoratech.com/dashboard/generated.txt"

# User input
user_input = input("Enter Training Code: ")

try:
    # Create a request with headers to mimic a browser request
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
except HTTPError as e:
    print("Error accessing the URL:", e)
else:
    # Proceed with the data processing
    print("Data loaded successfully.")
