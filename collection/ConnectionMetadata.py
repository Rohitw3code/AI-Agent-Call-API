from typing import Dict
from utils import endpoint_request
from custom_tool.tool import Tool


class ConnectionMetabody:
    export_metabody_data = {
        'data': True,
        'url': "/connectionMetabody/export",
        'req_type': 'POST'
    }

    convert_metabody_data = {
        'data': True,
        'url': "/connectionMetabody/convert",
        'req_type': 'POST'
    }

    @staticmethod
    def export_metabody():
        endpoint_request(
            url=ConnectionMetabody.export_metabody_data['url'],
            DATA=ConnectionMetabody.export_metabody_data['data'],
            req_type=ConnectionMetabody.export_metabody_data['req_type']
        )

    @staticmethod
    def convert_metabody():
        endpoint_request(
            url=ConnectionMetabody.convert_metabody_data['url'],
            DATA=ConnectionMetabody.convert_metabody_data['data'],
            req_type=ConnectionMetabody.convert_metabody_data['req_type']
        )


connection_metabody_export_tool = Tool(name="export_metabody",
                                       desc="It Exports connection metabody").get_tool()

connection_metabody_convert_tool = Tool(name="convert_metabody",
                                        desc="Converts connection metabody.").get_tool()


connection_meta_tools = [connection_metabody_export_tool,
                         connection_metabody_convert_tool]
