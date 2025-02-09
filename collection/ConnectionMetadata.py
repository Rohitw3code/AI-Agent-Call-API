from typing import Dict
from utils import endpoint_request


class ConnectionMetabody:
    @staticmethod
    def export_metabody(body: Dict):
        print(f"Method: export_metabody, Params: {body}")
        endpoint_request(url="/connectionMetabody/export", req_type='POST', body=body)

    @staticmethod
    def convert_metabody(body: Dict):
        print(f"Method: convert_metabody, Params: {body}")
        endpoint_request(url="/connectionMetabody/convert", req_type='POST', body=body)

connection_metabody_export_tool = {
    "type": "function",
    "function": {
            "name": "export_metabody",
            "description": "It Exports connection metabody",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "additionalProperties": False
            },
        "strict": True
    }
}

connection_metabody_convert_tool = {
    "type": "function",
    "function": {
            "name": "convert_metabody",
            "description": "Converts connection metabody.",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "additionalProperties": False
            },
        "strict": True
    }
}

connection_meta_tools = [connection_metabody_export_tool,
                        connection_metabody_convert_tool]



