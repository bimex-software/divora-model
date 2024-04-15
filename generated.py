import requests as req
import mysql.connector

# Database connection parameters
conn = mysql.connector.connect(
    host="s1106.usc1.mysecurecloudhost.com",
    user="divorate_account",
    password="694ddc20QQ@@",
    database="divorate_users"
)

# Check connection
if conn.is_connected():
    print("Connected to the database")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a SQL query to retrieve the training codes from the database
    cursor.execute("SELECT code FROM training_codes")

    # Fetch all the results
    rows = cursor.fetchall()

    # Extract training codes from the fetched results
    training_codes = [row[0] for row in rows]

    # Close cursor and connection
    cursor.close()
    conn.close()

    # User input
    user_input = input("Enter Training Code: ")

    if user_input in training_codes:
        # Grant access if the code is found in the database
        print("Access Granted")
    else:
        # Cause an error by trying to access an undefined variable
        undefined_variable

else:
    print("Failed to connect to the database")

