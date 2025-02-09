
class Tool:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.description = desc
        self.json_data = {
            "type": "function",
            "function": {
                "name": name,
                "description": desc,
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False
                },
                "strict": True
            }
        }
    
    def get_tool(self):
        return self.json_data


