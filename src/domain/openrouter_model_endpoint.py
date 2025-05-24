from pydantic import BaseModel
from typing import Union, Any


class OpenrouterModelEndpoint(BaseModel):
    name: str
    context_length: Union[int, str]
    pricing: Any
    provider_name: str
    tag: str
    quantization: Any
    max_prompt_tokens: Any
    supported_parameters: Any
    status: int

    def get_name(self) -> str:
        return self.name
    def get_provider_name(self) -> str:
        return self.provider_name
    def get_tag(self) -> str:
        return self.tag