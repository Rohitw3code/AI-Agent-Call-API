from custom_tool.tool import Tool
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


import_config_tool = Tool(name="import_config",
                          desc="import config archive").get_tool()

export_config_tool = Tool(name="export_config",
                          desc="export config archive").get_tool()


config_archive_tools = [import_config_tool,
                        export_config_tool]
