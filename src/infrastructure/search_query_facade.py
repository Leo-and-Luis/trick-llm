from typing import List
from rapidfuzz import process, fuzz
from pydantic import BaseModel

class SearchQueryFacade:
    def __init__(self):
        pass
    def get_matches_by_query(
            self,
            query: str,
            items: List[BaseModel],
            search_attr: str = "name",
            max_results: int = 5,
            score_threshold: int = 30
    ) -> List[BaseModel]:
        values = [getattr(item, search_attr, None) for item in items]

        # Remove items where the attribute does not exist or is None
        valid_indices = [i for i, val in enumerate(values) if isinstance(val, str)]
        values = [values[i] for i in valid_indices]
        valid_items = [items[i] for i in valid_indices]

        results = process.extract(
            query,
            values,
            scorer=fuzz.token_sort_ratio,
            limit=max_results
        )

        matched_items = [
            valid_items[idx] for name, score, idx in results if score >= score_threshold
        ]
        return matched_items