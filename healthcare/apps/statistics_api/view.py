from handler import ResponseHandler
from .service import StaticsService
from flask_restful import Resource
from flasgger import swag_from


class PatientTotalCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/patient_total_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.patient_total_count_s()

        return ResponseHandler(200).payload(res)


class EachGenderCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_gender_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_gender_count_s()

        return ResponseHandler(200).payload(res)


class EachRaceCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_race_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_race_count_s()

        return ResponseHandler(200).payload(res)


class EachEthnicityCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_ethnicity_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_ethnicity_count_s()

        return ResponseHandler(200).payload(res)


class PassAwayPersonCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/pass_away_person_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.pass_away_person_count_s()

        return ResponseHandler(200).payload(res)


class VisitTypeCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/visit_type_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.visit_type_count_s()

        return ResponseHandler(200).payload(res)


class VisitEachGenderCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_gender_visit_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_gender_visit_count_s()

        return ResponseHandler(200).payload(res)


class VisitEachRaceCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_race_visit_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_race_visit_count_s()

        return ResponseHandler(200).payload(res)


class VisitEachEthnicityCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_ethnicity_visit_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_ethnicity_visit_count_s()

        return ResponseHandler(200).payload(res)


class VisitEachGenerateCount(Resource):
    def __init__(self):
        self.static_service = StaticsService()

    @swag_from('swagger_doc/each_generate_visit_count.yml', methods=['GET'])
    def get(self):
        res = self.static_service.each_generate_visit_count_s()

        return ResponseHandler(200).payload(res)
