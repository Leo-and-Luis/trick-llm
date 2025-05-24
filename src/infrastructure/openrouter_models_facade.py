from typing import List
from src.domain.openrouter_model import OpenRouterModel
from rapidfuzz import process, fuzz
import requests

class OpenrouterModelsFacade:
    def __init__(self):
        self.url = "https://openrouter.ai/api/v1/models"
        self.models: List[OpenRouterModel] = []
    def get_all_models(self):
        response = requests.get(self.url)
        response.raise_for_status()
        raw = response.json()['data']
        models: List[OpenRouterModel] = [
            OpenRouterModel.model_validate(item) for item in raw
        ]
        return self.set_and_return_models(models)
    def set_and_return_models(self, models: List[OpenRouterModel]):
        self.models = models
        return models
    def get_models_by_query(
            self,
            query: str,
            max_results: int = 5,
            score_threshold: int = 30
    ) -> List[OpenRouterModel]:
        if not self.models:
            self.get_all_models()
        names = [model.name for model in self.models]
        results = process.extract(
            query,
            names,
            scorer=fuzz.token_sort_ratio,
            limit=max_results
        )
        matched_items = [
            self.models[idx] for name, score, idx in results if score >= score_threshold
        ]
        return matched_items


if __name__ == "__main__":
    openrouterModelsFacade = OpenrouterModelsFacade()
    while True:
        query = input("> ")
        models1 = openrouterModelsFacade.get_models_by_query(query)
        for model1 in models1:
            print(model1.name)
