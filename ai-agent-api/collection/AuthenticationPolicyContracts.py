import requests
from langchain.tools import Tool
from typing import Dict, Optional
from functools import partial
from credentials import HOST, USERNAME, PASSWORD, BASE_URL, HEADERS
from utils import endpoint_request

class AuthenticationPolicyContracts:
    @staticmethod
    def get_contracts(params: Optional[Dict] = None):
        print(f"Method: get_contracts, Params: {params}")
        endpoint_request(url="/authenticationPolicyContracts", param=params, req_type='GET')

    @staticmethod
    def create_contract(body: Dict):
        print(f"Method: create_contract, Params: body={body}")
        endpoint_request(url="/authenticationPolicyContracts", req_type='POST', body=body)

    @staticmethod
    def get_contract_by_id(contract_id: str):
        print(f"Method: get_contract_by_id, Params: contract_id={contract_id}")
        endpoint_request(url=f"/authenticationPolicyContracts/{contract_id}", req_type='GET')

    @staticmethod
    def update_contract(contract_id: str, body: Dict):
        print(f"Method: update_contract, Params: contract_id={contract_id}, body={body}")
        endpoint_request(url=f"/authenticationPolicyContracts/{contract_id}", req_type='PUT', body=body)

    @staticmethod
    def delete_contract(contract_id: str):
        print(f"Method: delete_contract, Params: contract_id={contract_id}")
        endpoint_request(url=f"/authenticationPolicyContracts/{contract_id}", req_type='DELETE')


authentication_policy_contracts_get_tool = Tool(
    name="Get Authentication Policy Contracts",
    func=partial(AuthenticationPolicyContracts.get_contracts),
    description="Fetches authentication policy contracts from PingFederate, optionally with query parameters."
)

authentication_policy_contracts_create_tool = Tool(
    name="Create Authentication Policy Contract",
    func=lambda body:AuthenticationPolicyContracts.create_contract(body),
    description="Creates a new authentication policy contract. body in dict"
)

authentication_policy_contracts_get_by_id_tool = Tool(
    name="Get Authentication Policy Contract by ID",
    func=lambda contract_id:AuthenticationPolicyContracts.get_contract_by_id(contract_id),
    description="Fetches an authentication policy using contract by ID  contact_id"
)

authentication_policy_contracts_update_tool = Tool(
    name="Update Authentication Policy Contract",
    func=lambda contract_id,body:AuthenticationPolicyContracts.update_contract(contract_id,body),
    description="Updates an existing authentication policy contract. Requires contract ID and body in dict"
)

authentication_policy_contracts_delete_tool = Tool(
    name="Delete Authentication Policy Contract",
    func=lambda contract_id:AuthenticationPolicyContracts.delete_contract(contract_id),
    description="Deletes an authentication policy contract by ID contact_id"
)

authentication_policy_contracts_tools = [
    authentication_policy_contracts_get_tool,
    authentication_policy_contracts_create_tool,
    authentication_policy_contracts_get_by_id_tool,
    authentication_policy_contracts_update_tool,
    authentication_policy_contracts_delete_tool
]
