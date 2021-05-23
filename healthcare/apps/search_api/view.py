from handler import ResponseHandler
from .service import SearchService
from flask_restful import Resource
from .inputdto import SearchDTO, ValidationError
from flask import request
from flasgger import swag_from


class ConceptSearch(Resource):
    def __init__(self):
        self.search_service = SearchService()

    @swag_from('swagger_doc/concept_search.yml', methods=['GET'])
    def get(self):
        try:
            concept_dto = SearchDTO(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(412).validator_response(v.json())

        res = self.search_service.concept_search(concept_dto.keyword, concept_dto.page)

        return ResponseHandler(200).payload(res)


class ConceptSearchCount(Resource):
    def __init__(self):
        self.search_service = SearchService()

    def get(self):
        try:
            concept_dto = SearchDTO(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(412).validator_response(v.json())

        res = self.search_service.concept_search_count(concept_dto.keyword)

        return ResponseHandler(200).payload(res)


class DrugSearch(Resource):
    def __init__(self):
        self.search_service = SearchService()

    @swag_from('swagger_doc/drug_search.yml', methods=['GET'])
    def get(self):
        try:
            concept_dto = SearchDTO(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(412).validator_response(v.json())

        res = self.search_service.drug_search(concept_dto.keyword, concept_dto.page)

        return ResponseHandler(200).payload(res)


class DrugSearchCount(Resource):
    def __init__(self):
        self.search_service = SearchService()

    def get(self):
        try:
            concept_dto = SearchDTO(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(412).validator_response(v.json())

        res = self.search_service.drug_search_count(concept_dto.keyword)

        return ResponseHandler(200).payload(res)


class ConditionSearch(Resource):
    def __init__(self):
        self.search_service = SearchService()

    @swag_from('swagger_doc/condition_search.yml', methods=['GET'])
    def get(self):
        try:
            concept_dto = SearchDTO(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(412).validator_response(v.json())

        res = self.search_service.condition_search(concept_dto.keyword, concept_dto.page)

        return ResponseHandler(200).payload(res)


class ConditionSearchCount(Resource):
    def __init__(self):
        self.search_service = SearchService()

    def get(self):
        try:
            concept_dto = SearchDTO(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(412).validator_response(v.json())

        res = self.search_service.condition_search_count(concept_dto.keyword)

        return ResponseHandler(200).payload(res)
