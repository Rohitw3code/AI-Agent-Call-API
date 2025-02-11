import streamlit as st
from credentials import HOST, USERNAME, PASSWORD, BASE_URL, HEADERS
from typing import Dict
import requests



def endpoint_request(url='', PARAM=False, DATA=False, req_type='GET'):  
    url = BASE_URL + url

    # param = PARAM if PARAM else {} 
    # data = DATA if DATA else {}  

    param = {}
    data = {}

    # print("Endpoint URL:", url)
    # print("Data:", data)
    # print("Param:", param)

    try:
        if req_type == 'GET':
            response = requests.get(url, params=param, headers=HEADERS, auth=(USERNAME, PASSWORD), verify=False)
        elif req_type == 'POST':
            response = requests.post(url, json=data, headers=HEADERS, auth=(USERNAME, PASSWORD), verify=False)
        elif req_type == 'PUT':
            response = requests.put(url, json=data, headers=HEADERS, auth=(USERNAME, PASSWORD), verify=False)
        elif req_type == 'DELETE':
            response = requests.delete(url, params=param, headers=HEADERS, auth=(USERNAME, PASSWORD), verify=False)
        else:
            error_msg = "ERROR: Invalid request type"
            st.error(error_msg)
            # return error_msg
        
        response.raise_for_status()
        st.success("Request completed successfully!")  # Success message
        return response.json()
    except requests.exceptions.RequestException as e:
        error_msg = f"ERROR: {str(e)}"
        st.error(error_msg)  # Display error in Streamlit
        # return error_msg