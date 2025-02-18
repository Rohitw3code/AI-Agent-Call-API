import requests
from langchain.tools import Tool
from typing import Dict, Optional
import os
from functools import partial
from credentials import HOST,USERNAME,PASSWORD,BASE_URL,HEADERS
from utils import endpoint_request


class AuthenticationPolicies:
    @staticmethod
    def get_policies(_: Optional[str] = None):
        print("Method: get_policies, Params: None")
        endpoint_request(url="/authenticationPolicies/settings", req_type='GET')

    @staticmethod
    def update_policies(body: Dict, id: Optional[str] = None):
        print(f"Method: update_policies, Params: body={body}, id={id}")
        url = f"/authenticationPolicies/settings/{id}"
        endpoint_request(url=url, req_type='PUT', body=body)

    @staticmethod
    def get_default(_: Optional[str] = None):
        print("Method: get_default, Params: None")
        endpoint_request(url="/authenticationPolicies/default", req_type='GET')

    @staticmethod
    def update_default(body: Dict):
        print(f"Method: update_default, Params: body={body}")
        endpoint_request(url="/authenticationPolicies/default", req_type='PUT', body=body)



authentication_policies_tool = Tool(
    name="Get Authentication Policies",
    func=partial(AuthenticationPolicies.get_policies),
    description="Fetches authentication policies settings from PingFederate."
)

authentication_policies_update_tool = Tool(
    name="Update Authentication Policies",
    func=lambda body, id: AuthenticationPolicies.update_policies(
        body, id),
    description="Updates authentication policies settings. body in dict and id"
)

authentication_policies_default_get_tool = Tool(
    name="Get Authentication Policies",
    func=partial(AuthenticationPolicies.get_default),
    description="Fetches authentication policies default from PingFederate."
)


authentication_policies_default_update_tool = Tool(
    name="Update Authentication Policies",
    func=lambda body : AuthenticationPolicies.update_default(
        body),
    description="Updates authentication policies default. body in dict"
)


authentication_policies_tools = [
    authentication_policies_tool, 
    authentication_policies_update_tool,
    authentication_policies_default_get_tool,
    authentication_policies_default_update_tool]
