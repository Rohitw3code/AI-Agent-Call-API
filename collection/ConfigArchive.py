from custom_tool.tool import Tool
from utils import endpoint_request

class ConfigArchive:
    import_config_data = {
        'url': "/configArchive/import",
        'param': True,
        'req_type': "POST",
        'data':False
    }

    export_config_data = {
        'url': "/configArchive/export",
        'req_type': "GET",
        'param':False,
        'data':False
    }

    @staticmethod
    def import_config():
        return endpoint_request(
            url=ConfigArchive.import_config_data['url'],
            PARAM=ConfigArchive.import_config_data['param'],
            req_type=ConfigArchive.import_config_data['req_type']
        )

    @staticmethod
    def export_config():
        return endpoint_request(
            url=ConfigArchive.export_config_data['url'],
            req_type=ConfigArchive.export_config_data['req_type']
        )

import_config_tool = Tool(name="import_config",
                          desc="import config archive").get_tool()

export_config_tool = Tool(name="export_config",
                          desc="export config archive").get_tool()

config_archive_tools = [import_config_tool, export_config_tool]
