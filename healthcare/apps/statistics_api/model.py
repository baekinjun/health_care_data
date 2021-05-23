from db import Procedure


class StaticsDao:
    def __init__(self):
        self.conn_s = Procedure()

    def patient_total_count_d(self):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as count FROM person"""
        )

    def each_gender_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT gender_source_value as gender ,COUNT(gender_concept_id) as count
                FROM person group by gender_source_value;"""
        )

    def each_race_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT race_source_value as race_person, COUNT(race_concept_id) as count
                FROM person GROUP BY race_source_value;"""
        )

    def each_ethnicity_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT ethnicity_source_value as ethnicity , COUNT(ethnicity_concept_id) as count
                FROM person GROUP BY ethnicity_source_value;"""
        )

    def pass_away_person_count_d(self):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as pass_away_person_count FROM death;"""
        )

    def visit_type_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT co.concept_name,COUNT(vo.visit_concept_id) FROM visit_occurrence as vo
                JOIN concept as co ON vo.visit_concept_id = co.concept_id
                GROUP BY co.concept_name;"""
        )

    def each_gender_visit_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT ps.gender_source_value as gender,COUNT(ps.gender_concept_id) as count FROM person as ps
                JOIN visit_occurrence as vo ON ps.person_id = vo.person_id
                GROUP BY ps.gender_source_value;"""
        )

    def each_race_visit_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT ps.race_source_value as race_person,COUNT(ps.race_concept_id) as count FROM person as ps
                JOIN visit_occurrence as vo ON ps.person_id = vo.person_id
                GROUP BY ps.race_source_value;"""
        )

    def each_ethnicity_visit_count_d(self):
        return self.conn_s.b_fetchall(
            """SELECT ps.ethnicity_source_value as ethnicity,COUNT(ps.ethnicity_concept_id) as count FROM person as ps
                JOIN visit_occurrence as vo ON ps.person_id = vo.person_id
                GROUP BY ps.ethnicity_source_value;"""
        )

    def each_generate_visit_count_d(self):
        return self.conn_s.b_fetchall(
            """select floor (EXTRACT (year FROM age(vo.visit_start_datetime,ps.birth_datetime))/10)*10 as generation,
                COUNT(ps.person_id) as count
                from person as ps join visit_occurrence as vo 
                ON ps.person_id = vo.person_id
                group by generation order by generation;"""
        )
