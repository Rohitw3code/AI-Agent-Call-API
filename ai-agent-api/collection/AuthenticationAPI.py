import requests
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from typing import Dict, Optional
import os
from functools import partial
from credentials import HOST,USERNAME,PASSWORD,BASE_URL,HEADERS
from utils import endpoint_request


class AuthenticationAPI:
    @staticmethod
    def get_settings(_: Optional[str] = None):
        print("Method: get_settings, Params: None")
        endpoint_request(url="/authenticationApi/settings", req_type='GET')

    @staticmethod
    def update_settings(body: Dict):
        print(f"Method: update_settings, Params: body={body}")
        endpoint_request(url="/authenticationApi/settings", req_type='PUT', body=body)

    @staticmethod
    def get_application(_: Optional[str] = None):
        print("Method: get_application, Params: None")
        endpoint_request(url="/authenticationApi/applications", req_type='GET')

    @staticmethod
    def post_application(body: Dict):
        print(f"Method: post_application, Params: body={body}")
        endpoint_request(url="/authenticationApi/applications", req_type='POST', body=body)

    @staticmethod
    def get_application_by_id(id_: int):
        print(f"Method: get_application_by_id, Params: id_={id_}")
        endpoint_request(url=f"/authenticationApi/applications/{id_}", req_type='GET')
    
    @staticmethod
    def update_application_by_id(id_: int, body: Dict):
        print(f"Method: update_application_by_id, Params: id_={id_}, body={body}")
        endpoint_request(url=f"/authenticationApi/applications/{id_}", req_type='PUT', body=body)

    @staticmethod
    def delete_application_by_id(id_: int):
        print(f"Method: delete_application_by_id, Params: id_={id_}")
        endpoint_request(url=f"/authenticationApi/applications/{id_}", req_type='DELETE')



authentication_get_settings = Tool(
    name="Get Authentication Settings",
    func=partial(AuthenticationAPI.get_settings),
    description="Fetches authentication API settings from PingFederate."
)

authentication_api_update_settings = Tool(
    name="Update Authentication Settings",
    func=lambda body: AuthenticationAPI.update_settings(body),
    description="Updates authentication API settings. body in dict  with API enablement, default application reference, and API descriptions toggle."
)

authentication_api_fetch_settings = Tool(
    name="Fetch Authentication Application Settings",
    func=partial(AuthenticationAPI.get_application),
    description="Retrieves the authentication application settings, including configurations and policies."
)

authentication_api_post_application = Tool(
    name="Create Authentication Application",
    func=lambda body: AuthenticationAPI.post_application(body),
    description="Creates a new authentication application using the body in dict"
)

authentication_api_fetch_application = Tool(
    name="Fetch Authentication Application by ID",
    func=lambda id_: AuthenticationAPI.get_application_by_id(id_),
    description="Fetches details of a specific authentication application using its unique ID."
)

authentication_api_update_by_id = Tool(
    name="Update Authentication Application by ID",
    func=lambda id_: AuthenticationAPI.update_application_by_id(id_),
    description="Updates an existing authentication application identified by its unique ID. Requires a JSON payload with updated settings."
)

authentication_api_delete_by_id = Tool(
    name="Delete Authentication Application by ID",
    func=lambda id_: AuthenticationAPI.delete_application_by_id(id_),
    description="Deletes an authentication application using its unique ID."
)

authentication_api_tools = [authentication_get_settings,authentication_api_update_settings, authentication_api_fetch_settings,
                      authentication_api_post_application,authentication_api_fetch_application, authentication_api_update_by_id,
                      authentication_api_delete_by_id]
