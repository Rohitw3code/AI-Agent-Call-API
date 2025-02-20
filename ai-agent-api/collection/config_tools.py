from utils import endpoint_request
from langchain_core.tools import tool
from .endpoint_data import *

@tool
def get_sp_connections():
    "Fetch service provider connections"
    print("called get_sp_connections endpoint ", "=" * 10)
    return endpoint_request(
        url=get_sp_connections_data['url'],
        req_type=get_sp_connections_data['req_type'],
        param=get_sp_connections_data['param'],
        data=get_sp_connections_data['data']
    )

@tool
def create_sp_connections():
    "Create service provider connection"
    print("called create_sp_connections endpoint ", "=" * 10)
    return endpoint_request(
        url=create_sp_connections_data['url'],
        req_type=create_sp_connections_data['req_type'],
        param=create_sp_connections_data['param'],
        data=create_sp_connections_data['data']
    )

@tool
def get_sp_connection_by_id():
    "Fetch a specific service provider connection by ID"
    print("called get_sp_connection_by_id endpoint ", "=" * 10)
    return endpoint_request(
        url=get_sp_connection_by_id_data['url'].format(id=1),
        req_type=get_sp_connection_by_id_data['req_type'],
        param=get_sp_connection_by_id_data['param'],
        data=get_sp_connection_by_id_data['data']
    )

@tool
def update_sp_connection():
    "Update a specific service provider connection by ID"
    print("called update_sp_connection endpoint ", "=" * 10)
    return endpoint_request(
        url=update_sp_connection_data['url'].format(id=1),
        req_type=update_sp_connection_data['req_type'],
        param=update_sp_connection_data['param'],
        data=update_sp_connection_data['data']
    )

@tool
def delete_sp_connection():
    "Delete a specific service provider connection by ID"
    print("called delete_sp_connection endpoint ", "=" * 10)
    return endpoint_request(
        url=delete_sp_connection_data['url'].format(id=1),
        req_type=delete_sp_connection_data['req_type'],
        param=delete_sp_connection_data['param'],
        data=delete_sp_connection_data['data']
    )

@tool
def get_signing_settings():
    "Fetch signing settings for a specific service provider connection by ID"
    print("called get_signing_settings endpoint ", "=" * 10)
    return endpoint_request(
        url=get_signing_settings_data['url'].format(id=1),
        req_type=get_signing_settings_data['req_type'],
        param=get_signing_settings_data['param'],
        data=get_signing_settings_data['data']
    )

@tool
def update_signing_settings(data: dict):
    "Update signing settings for a specific service provider connection by ID"
    print("called update_signing_settings endpoint ", "=" * 10)
    return endpoint_request(
        url=update_signing_settings_data['url'].format(id=1),
        req_type=update_signing_settings_data['req_type'],
        param=update_signing_settings_data['param'],
        data=update_signing_settings_data['data']
    )

@tool
def add_sp_connection_cert(data: dict):
    "Add a certificate to a specific service provider connection by ID"
    print("called add_sp_connection_cert endpoint ", "=" * 10)
    return endpoint_request(
        url=add_sp_connection_cert_data['url'].format(id=1),
        req_type=add_sp_connection_cert_data['req_type'],
        param=add_sp_connection_cert_data['param'],
        data=add_sp_connection_cert_data['data']
    )

@tool
def get_sp_connection_certs():
    "Fetch certificates for a specific service provider connection by ID"
    print("called get_sp_connection_certs endpoint ", "=" * 10)
    return endpoint_request(
        url=get_sp_connection_certs_data['url'].format(id=1),
        req_type=get_sp_connection_certs_data['req_type'],
        param=get_sp_connection_certs_data['param'],
        data=get_sp_connection_certs_data['data']
    )

@tool
def update_sp_connection_certs(data: dict):
    "Update certificates for a specific service provider connection by ID"
    print("called update_sp_connection_certs endpoint ", "=" * 10)
    return endpoint_request(
        url=update_sp_connection_certs_data['url'].format(id=1),
        req_type=update_sp_connection_certs_data['req_type'],
        param=update_sp_connection_certs_data['param'],
        data=update_sp_connection_certs_data['data']
    )

@tool
def get_sp_connection_decryption_keys():
    "Fetch decryption keys for a specific service provider connection by ID"
    print("called get_sp_connection_decryption_keys endpoint ", "=" * 10)
    return endpoint_request(
        url=get_sp_connection_decryption_keys_data['url'].format(id=1),
        req_type=get_sp_connection_decryption_keys_data['req_type'],
        param=get_sp_connection_decryption_keys_data['param'],
        data=get_sp_connection_decryption_keys_data['data']
    )

@tool
def update_sp_connection_decryption_keys(data: dict):
    "Update decryption keys for a specific service provider connection by ID"
    print("called update_sp_connection_decryption_keys endpoint ", "=" * 10)
    return endpoint_request(
        url=update_sp_connection_decryption_keys_data['url'].format(id=1),
        req_type=update_sp_connection_decryption_keys_data['req_type'],
        param=update_sp_connection_decryption_keys_data['param'],
        data=update_sp_connection_decryption_keys_data['data']
    )

# Consolidated list of all tools
idp_sp_tools = [
    get_sp_connections, create_sp_connections, get_sp_connection_by_id, update_sp_connection, delete_sp_connection,
    get_signing_settings, update_signing_settings, add_sp_connection_cert, get_sp_connection_certs,
    update_sp_connection_certs, get_sp_connection_decryption_keys, update_sp_connection_decryption_keys
]
