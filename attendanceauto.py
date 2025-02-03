import streamlit as st
import json

# Simulate receiving JSON data from query parameters
st.title("Streamlit JSON Receiver")

# Get the query parameters using experimental API
query_params = st.query_params

# Get JSON from query param 'data'
json_data = query_params.get('data', [None])[0]

if json_data:
    # Parse the received JSON data
    try:
        data = json.loads(json_data)
        st.write("Received JSON data:", data)
    except json.JSONDecodeError:
        st.write("Invalid JSON data.")
else:
    st.write("No JSON data received.")
