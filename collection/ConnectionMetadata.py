from typing import Dict
from utils import endpoint_request
from custom_tool.tool import Tool

class ConnectionMetabody:
    @staticmethod
    def export_metabody(body: Dict):
        print(f"Method: export_metabody, Params: {body}")
        endpoint_request(url="/connectionMetabody/export", req_type='POST', body=body)

    @staticmethod
    def convert_metabody(body: Dict):
        print(f"Method: convert_metabody, Params: {body}")
        endpoint_request(url="/connectionMetabody/convert", req_type='POST', body=body)


connection_metabody_export_tool = Tool(name="export_metabody",
                                       desc="It Exports connection metabody").get_tool()

connection_metabody_convert_tool = Tool(name="convert_metabody",
                                       desc="Converts connection metabody.").get_tool()


connection_meta_tools = [connection_metabody_export_tool,
                        connection_metabody_convert_tool]



