from utils import endpoint_request
from langchain_core.tools import tool
from .endpoint_data import config_archive_import_data,config_archive_export_data



@tool
def config_archive_export():
    "config archive export"
    return endpoint_request(**config_archive_export_data)



@tool
def config_archive_import():
    "config archive import"
    return endpoint_request(**config_archive_import_data)

config_archive_tools = [config_archive_export,config_archive_import]