from typing import List
from pydantic import BaseModel
from src.domain.openrouter_model import OpenrouterModel
from src.infrastructure.search_query_facade import SearchQueryFacade
import requests

class OpenrouterModelsFacade:
    def __init__(self):
        self.url = "https://openrouter.ai/api/v1/models"
        self.models: List[OpenrouterModel] = []
        self.search_query_facade = SearchQueryFacade()
    def get_all_models(self):
        response = requests.get(self.url)
        response.raise_for_status()
        raw = response.json()['data']
        models: List[OpenrouterModel] = [
            OpenrouterModel.model_validate(item) for item in raw
        ]
        return self.set_and_return_models(models)
    def set_and_return_models(self, models: List[OpenrouterModel]):
        self.models = models
        return models
    def get_models_by_query(
            self,
            query: str,
            max_results: int = 5,
            score_threshold: int = 30
    ) -> list[BaseModel]:
        if not self.models:
            self.get_all_models()
        matched_items = self.search_query_facade.get_matches_by_query(query, self.models, "name", max_results, score_threshold)
        return matched_items


if __name__ == "__main__":
    openrouterModelsFacade = OpenrouterModelsFacade()
    while True:
        query1 = input("> ")
        models1 = openrouterModelsFacade.get_models_by_query(query1)
        for model1 in models1:
            print(model1.name)
