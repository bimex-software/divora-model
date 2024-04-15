import urllib.request

# Load the online text file
url = "https://user-final.shilohpendergra.repl.co/dashboard/generated.txt"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

# User input
user_input = input("Enter Training Code: ")
