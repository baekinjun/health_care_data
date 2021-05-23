from .model import SearchDao
from flask import jsonify


class SearchService:
    def __init__(self):
        self.search_dao = SearchDao()

    def concept_search(self, keyword, page):
        if keyword:
            res = self.search_dao.concept_keyword_search(("%" + keyword + "%", page))
        else:
            res = self.search_dao.total_concept([page])

        return res

    def concept_search_count(self, keyword):
        if keyword:
            res = self.search_dao.concept_keyword_count(["%" + keyword + "%"])
        else:
            res = self.search_dao.total_concept_count()

        return res

    def drug_search(self, keyword, page):
        if keyword:
            res = self.search_dao.drug_keyword_search(("%" + keyword + "%", page))
        else:
            res = self.search_dao.total_drug([page])

        return res

    def drug_search_count(self, keyword):
        if keyword:
            res = self.search_dao.drug_keyword_count(["%" + keyword + "%"])
        else:
            res = self.search_dao.total_drug_count()

        return res

    def condition_search(self, keyword, page):
        if keyword:
            res = self.search_dao.condition_keyword_search(("%" + keyword + "%", page))
        else:
            res = self.search_dao.total_condition([page])

        return res

    def condition_search_count(self, keyword):
        if keyword:
            res = self.search_dao.condition_keyword_count(["%" + keyword + "%"])
        else:
            res = self.search_dao.total_condition_count()

        return res
