import urllib.request
from urllib.error import HTTPError

# Define the encryption method for the URL
def encrypt_url():
    encrypted_url = ''.join(chr(i) for i in [104, 116, 116, 112, 115, 58, 47, 47, 100, 105, 118, 111, 114, 97, 116, 101, 99, 104, 46, 99, 111, 109, 47, 100, 97, 115, 104, 98, 111, 97, 114, 100, 47, 103, 101, 110, 101, 114, 97, 116, 101, 100, 46, 116, 120, 116])
    return encrypted_url

# Load the online text file
url = encrypt_url()

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