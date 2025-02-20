# endpoint_data.py

# GET /idp/spConnections
get_sp_connections_data = {
    'url': "/idp/spConnections",
    'req_type': "GET",
    'param': {
        "entityId": "",
        "page": "",
        "numberPerPage": "",
        "filter": ""
    },
    'data': {}
}

# POST /idp/spConnections
create_sp_connections_data = {
    'url': "/idp/spConnections",
    'req_type': "POST",
    'param': {},
    'data': {}
}

# GET /idp/spConnections/{id}
get_sp_connection_by_id_data = {
    'url': "/idp/spConnections/{id}",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}
update_sp_connection_data = {
    'url': "/idp/spConnections/{id}",
    'req_type': "PUT",
    'param': {},
    'data': {}
}

# DELETE /idp/spConnections/{id}
delete_sp_connection_data = {
    'url': "/idp/spConnections/{id}",
    'req_type': "DELETE",
    'param': {},
    'data': {}
}

# GET /idp/spConnections/{id}/credentials/signingSettings
get_signing_settings_data = {
    'url': "/idp/spConnections/{id}/credentials/signingSettings",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}/credentials/signingSettings
update_signing_settings_data = {
    'url': "/idp/spConnections/{id}/credentials/signingSettings",
    'req_type': "PUT",
    'param': {},
    'data': {}
}

# POST /idp/spConnections/{id}/credentials/certs
add_sp_connection_cert_data = {
    'url': "/idp/spConnections/{id}/credentials/certs",
    'req_type': "POST",
    'param': {},
    'data': {}
}

# GET /idp/spConnections/{id}/credentials/certs
get_sp_connection_certs_data = {
    'url': "/idp/spConnections/{id}/credentials/certs",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}/credentials/certs
update_sp_connection_certs_data = {
    'url': "/idp/spConnections/{id}/credentials/certs",
    'req_type': "PUT",
    'param': {},
    'data': {}
}

# GET /idp/spConnections/{id}/credentials/decryptionKeys
get_sp_connection_decryption_keys_data = {
    'url': "/idp/spConnections/{id}/credentials/decryptionKeys",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}/credentials/decryptionKeys
update_sp_connection_decryption_keys_data = {
    'url': "/idp/spConnections/{id}/credentials/decryptionKeys",
    'req_type': "PUT",
    'param': {},
    'data': {}
}
