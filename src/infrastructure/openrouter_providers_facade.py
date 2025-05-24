import requests
from src.domain.openrouter_model import OpenrouterModel
from src.domain.openrouter_model_endpoint import OpenrouterModelEndpoint
from src.infrastructure.openrouter_models_facade import OpenrouterModelsFacade
from typing import List

class OpenrouterProvidersFacade:
    def __init__(self):
        pass
    def get_model_endpoints(self, model: OpenrouterModel):
        author, _, slug = model.id.partition("/")
        url = f"https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints"
        response = requests.get(url)
        raw = response.json()['data']['endpoints']
        endpoints: List[OpenrouterModelEndpoint] = [
            OpenrouterModelEndpoint.model_validate(item) for item in raw
        ]
        return endpoints



if __name__ == "__main__":
    openrouterProvidersFacade = OpenrouterProvidersFacade()
    openrouterModelsFacade = OpenrouterModelsFacade()
    models = openrouterModelsFacade.get_all_models()
    endpoints1 = openrouterProvidersFacade.get_model_endpoints(models[2])
    for endpoint in endpoints1:
        print(endpoint.get_tag())