from utils import endpoint_request
from langchain_core.tools import tool
from .endpoint_data import export_metabody_data,convert_metabody_data


@tool
def export_metabody():
    "export the connection metadata"
    return endpoint_request(**export_metabody_data)

@tool
def convert_metabody():
    "convert the connection metadata"
    return endpoint_request(**convert_metabody_data)




connection_meta_tools = [export_metabody,
                         convert_metabody]