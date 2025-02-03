import streamlit as st
import json

# Simulate receiving JSON data from query parameters
st.title("Streamlit JSON Receiver")

# Get query parameters using experimental API
query_params = st.query_params

# Check if the action is 'register'
if query_params.get("action") == ["register"]:

    # Get JSON from query param 'data'
    json_data = query_params.get('data', [None])[0]
    
    if json_data:
        # Parse the received JSON data
        try:
            data = json.loads(json_data)
            file_name = "sample_text_file.txt"
            
            # Retrieve values from the JSON data
            userdetails = f"{data.get('name')}, {data.get('networkName')}, {data.get('classname')}"
            
            # Write the user details to a text file
            with open(file_name, "w") as file:
                file.write(userdetails)
            
            st.write("Received JSON data:", data)
        except json.JSONDecodeError:
            st.write("Invalid JSON data.")
    else:
        st.write("No JSON data received.")
else:
    try:
        # Read and display the content of the file if not registering
        with open("sample_text_file.txt", "r") as file:
            file_content = file.read()
        st.write("File Content:")
        st.text(file_content)
    except FileNotFoundError:
        st.write("File not found. Please register first.")
