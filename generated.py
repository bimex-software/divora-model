import urllib.request

# Load the online text file
url = "https://divoratech.com/dashboard/generated.txt"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

# User input
user_input = input("Enter Training Code: ")
