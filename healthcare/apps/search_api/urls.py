from .view import *

url_patterns = [
    (ConceptSearch, '/concept_search'),
    (ConceptSearchCount, '/concept_search_count'),
    (DrugSearch, '/drug_search'),
    (DrugSearchCount, '/drug_search_count'),
    (ConditionSearch, '/condition_search'),
    (ConditionSearchCount, '/condition_search_count')
]
