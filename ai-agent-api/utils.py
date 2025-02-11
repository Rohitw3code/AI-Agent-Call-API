import streamlit as st
from credentials import HOST, USERNAME, PASSWORD, BASE_URL, HEADERS
from typing import Dict
import requests



def endpoint_request(url='', param={}, data={}, req_type='GET'):  
    url = BASE_URL + url

    print("Endpoint URL:", url)
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
            return error_msg
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_msg = f"ERROR: {str(e)}"
        return error_msg