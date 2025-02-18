from utils import endpoint_request
from langchain_core.tools import tool

import_config_data = {
    'url': "/configArchive/import",
    'param': {"forceImport": True},
    'req_type': "POST",
    'data': {}
}

export_config_data = {
    'url': "/configArchive/export",
    'req_type': "GET",
    'param': {},
    'data': {}
}

@tool
def import_config():
    "import config endpoint"
    return endpoint_request(
        url=import_config_data['url'],
        param=import_config_data['param'],
        req_type=import_config_data['req_type']
    )

@tool
def export_config():
    "export config endpoint"
    return endpoint_request(
        url=export_config_data['url'],
        req_type=export_config_data['req_type']
    )


config_archive_tools = [export_config,import_config]