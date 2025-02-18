from collection.ConfigArchive import import_config,export_config,import_config_data,export_config_data
from collection.ConnectionMetadata import convert_metabody,export_metabody,convert_metabody_data,export_metabody_data


TOOL_MAPPING = {
    "import_config": (import_config, import_config_data),
    "export_config": (export_config, export_config_data),
    "convert_metabody":(convert_metabody,convert_metabody_data),
    "export_metabody":(export_metabody,export_metabody_data)
}