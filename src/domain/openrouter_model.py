from pydantic import BaseModel
from typing import Any, List, Optional, Union

class OpenrouterModel(BaseModel):
    id: str
    hugging_face_id: Optional[str] = None
    name: str
    created: int
    description: str
    context_length: Union[int, str]  # <== fix here
    architecture: Any
    pricing: Any
    top_provider: Any
    per_request_limits: Any
    supported_parameters: List[str]