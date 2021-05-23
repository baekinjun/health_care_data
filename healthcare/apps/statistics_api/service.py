from .model import StaticsDao


class StaticsService:
    def __init__(self):
        self.statics_dao = StaticsDao()

    def patient_total_count_s(self):
        res = self.statics_dao.patient_total_count_d()

        return res

    def each_gender_count_s(self):
        res = self.statics_dao.each_gender_count_d()

        return res

    def each_race_count_s(self):
        res = self.statics_dao.each_race_count_d()

        return res

    def each_ethnicity_count_s(self):
        res = self.statics_dao.each_ethnicity_count_d()

        return res

    def pass_away_person_count_s(self):
        res = self.statics_dao.pass_away_person_count_d()

        return res

    def visit_type_count_s(self):
        res = self.statics_dao.visit_type_count_d()

        return res

    def each_gender_visit_count_s(self):
        res = self.statics_dao.each_gender_visit_count_d()

        return res

    def each_race_visit_count_s(self):
        res = self.statics_dao.each_race_visit_count_d()

        return res

    def each_ethnicity_visit_count_s(self):
        res = self.statics_dao.each_ethnicity_visit_count_d()

        return res

    def each_generate_visit_count_s(self):
        res = self.statics_dao.each_generate_visit_count_d()

        return res
