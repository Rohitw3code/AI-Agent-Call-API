from utils import endpoint_request


class ConfigArchive:
    @staticmethod
    def import_config():
        """Calls the import configuration API endpoint"""
        param = {}
        print("param : ", param)
        url = "/configArchive/import"
        endpoint_request(url=url, param=param, req_type="POST")

    @staticmethod
    def export_config():
        """Calls the export configuration API endpoint"""
        url = "/configArchive/export"
        endpoint_request(url, {}, "GET")


import_config_tool = {
    "type": "function",
    "function": {
            "name": "import_config",
            "description": "import config archive",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "additionalProperties": False
            },
        "strict": True
    }
}

export_config_tool = {
    "type": "function",
    "function": {
            "name": "export_config",
            "description": "export config archive",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "additionalProperties": False
            },
        "strict": True
    }
}

config_archive_tools = [import_config_tool,
                        export_config_tool]
