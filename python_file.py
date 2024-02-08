if user_input in python_script:
    print("Access granted")
    # Execute the Python script
    exec(python_script)
else:
    print("Access denied")