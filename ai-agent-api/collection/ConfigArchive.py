from utils import endpoint_request
from langchain_core.tools import tool
import json

# Config Archive Endpoints
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
    return json.dumps(endpoint_request(
        url=import_config_data['url'],
        param=import_config_data['param'],
        req_type=import_config_data['req_type']
    ))

@tool
def export_config():
    "export config endpoint"
    return json.dumps(endpoint_request(
        url=export_config_data['url'],
        req_type=export_config_data['req_type']
    ))

# Current Time Endpoint
@tool
def get_current_time():
    "get current time endpoint"
    return json.dumps(endpoint_request(url="/time/current", req_type="GET"))

# General Data Endpoints
@tool
def get_user():
    "get user data"
    return json.dumps(endpoint_request(url="/data/user", req_type="GET"))

@tool
def get_posts():
    "get posts data"
    return json.dumps(endpoint_request(url="/data/posts", req_type="GET"))

@tool
def get_comments():
    "get comments data"
    return json.dumps(endpoint_request(url="/data/comments", req_type="GET"))

@tool
def get_likes():
    "get likes data"
    return json.dumps(endpoint_request(url="/data/likes", req_type="GET"))

@tool
def get_notifications():
    "get notifications data"
    return json.dumps(endpoint_request(url="/data/notifications", req_type="GET"))

config_archive_tools = [export_config, import_config]
data_tools = [get_user, get_posts, get_comments, get_likes, get_notifications]
time_tools = [get_current_time]

config_archive_tools.extend(data_tools)
config_archive_tools.extend(time_tools)
