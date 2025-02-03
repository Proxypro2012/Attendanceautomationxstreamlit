import streamlit as st
import json

# Simulate receiving JSON data from query parameters
st.title("Streamlit JSON Receiver")

query_params = st.query_params

# Get JSON from query param 'data'
json_data = query_params.get('data', [None])[0]

if json_data:
    # Parse the received JSON data
    try:
        data = json.loads(json_data)
        st.write("Received JSON data:", data)
        with open("sample_file.txt", "w") as f:
            f.write(data)

    
        with open("sample_file.txt", "r") as file:
            st.download_button(
                label="Download text file",
                data=file,
                file_name="sample_file.txt",
                mime="text/plain"
            )
    except json.JSONDecodeError:
        st.write("Invalid JSON data.")
else:
    st.write("No JSON data received.")
