from collection.endpoint_data import convert_metabody_data, export_metabody_data
from collection.SpConnection import (
    get_sp_connections, create_sp_connections, get_sp_connection_by_id, update_sp_connection,
    delete_sp_connection, get_signing_settings, update_signing_settings, add_sp_connection_cert,
    get_sp_connection_certs, update_sp_connection_certs, get_sp_connection_decryption_keys,
    update_sp_connection_decryption_keys
)
from collection.SpConnection import (
    get_sp_connections_data, create_sp_connections_data, get_sp_connection_by_id_data, update_sp_connection_data,
    delete_sp_connection_data, get_signing_settings_data, update_signing_settings_data, add_sp_connection_cert_data,
    get_sp_connection_certs_data, update_sp_connection_certs_data, get_sp_connection_decryption_keys_data,
    update_sp_connection_decryption_keys_data
)

from collection.configArchive import config_archive_export,config_archive_import ,config_archive_export_data,config_archive_import_data
from collection.ConnectionMetadata import convert_metabody,export_metabody,export_metabody_data,convert_metabody_data

TOOL_MAPPING = {
    "config_archive_export":(config_archive_export,config_archive_export_data),
    "config_archive_import":(config_archive_import,config_archive_import_data),

    # Connection Metadata Tools
    "convert_metabody": (convert_metabody, convert_metabody_data),
    "export_metabody": (export_metabody, export_metabody_data),

    # Service Provider Connection Tools
    "get_sp_connections": (get_sp_connections, get_sp_connections_data),
    "create_sp_connections": (create_sp_connections, create_sp_connections_data),
    "get_sp_connection_by_id": (get_sp_connection_by_id, get_sp_connection_by_id_data),
    "update_sp_connection": (update_sp_connection, update_sp_connection_data),
    "delete_sp_connection": (delete_sp_connection, delete_sp_connection_data),
    
    # Signing Settings
    "get_signing_settings": (get_signing_settings, get_signing_settings_data),
    "update_signing_settings": (update_signing_settings, update_signing_settings_data),

    # Certificates
    "add_sp_connection_cert": (add_sp_connection_cert, add_sp_connection_cert_data),
    "get_sp_connection_certs": (get_sp_connection_certs, get_sp_connection_certs_data),
    "update_sp_connection_certs": (update_sp_connection_certs, update_sp_connection_certs_data),

    # Decryption Keys
    "get_sp_connection_decryption_keys": (get_sp_connection_decryption_keys, get_sp_connection_decryption_keys_data),
    "update_sp_connection_decryption_keys": (update_sp_connection_decryption_keys, update_sp_connection_decryption_keys_data)
}
