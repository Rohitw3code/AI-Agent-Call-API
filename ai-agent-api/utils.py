import logging
import requests
import json
from credentials import HOST, USERNAME, PASSWORD, BASE_URL, HEADERS
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def execute_request(url: str, param: Dict, data: Dict, req_type: str):
    """Handles API requests with better error handling and logging."""
    full_url = BASE_URL + url
    headers = HEADERS
    auth = (USERNAME, PASSWORD)

    try:
        logging.info(f"Calling API: {full_url} | Type: {req_type} | Params: {param} | Body: {data}")

        response = requests.request(
            method=req_type,
            url=full_url,
            params=param if req_type in ["GET", "DELETE"] else None,
            json=data if req_type in ["POST", "PUT"] else None,
            headers=headers,
            auth=auth,
            verify=False
        )

        response.raise_for_status()
        logging.info(f"Response: {response.status_code} | {response.text[:100]}")
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"API Request Failed: {str(e)}")
        return {"error": str(e)}

def endpoint_request(url: str = '', param: Dict = {}, data: Dict = {}, req_type: str = 'GET'):
    """Wrapper function to execute API requests."""
    return execute_request(url, param, data, req_type)
