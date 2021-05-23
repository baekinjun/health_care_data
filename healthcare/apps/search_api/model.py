from db import Procedure


class SearchDao:
    def __init__(self):
        self.conn_s = Procedure()

    def total_concept(self, page):
        return self.conn_s.b_fetchall(
            """SELECT concept_id,concept_name,domain_id FROM concept LIMIT 10 OFFSET 10 * %s;""",
            page
        )

    def total_concept_count(self):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as count FROM concept"""
        )

    def concept_keyword_search(self, args):
        return self.conn_s.b_fetchall(
            """SELECT concept_id,concept_name,domain_id FROM concept where concept_name LIKE %s LIMIT 10 OFFSET 10 * %s;""",
            args
        )

    def concept_keyword_count(self, args):
        return self.conn_s.b_fetchall(
            """SELECT COUNT(*) as count FROM concept where concept_name LIKE %s;""",
            args
        )

    def drug_keyword_search(self, args):
        return self.conn_s.b_fetchall(
            """SELECT de.person_id,de.drug_concept_id,co.concept_name as drug_source_value,
                de.drug_exposure_start_datetime,de.drug_exposure_end_datetime,de.visit_occurrence_id
                from drug_exposure as de
                join concept as co on de.drug_concept_id=co.concept_id
                where co.concept_name LIKE %s
                LIMIT 10 OFFSET 10 * %s""",
            args
        )

    def drug_keyword_count(self, args):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as count
                from drug_exposure as de
                join concept as co on de.drug_concept_id=co.concept_id
                where co.concept_name LIKE %s""", args
        )

    def total_drug(self, args):
        return self.conn_s.b_fetchall(
            """SELECT de.person_id,de.drug_concept_id,co.concept_name as drug_source_value,
                de.drug_exposure_start_datetime,de.drug_exposure_end_datetime,de.visit_occurrence_id
                from drug_exposure as de
                join concept as co on de.drug_concept_id=co.concept_id
                LIMIT 10 OFFSET 10 * %s""",
            args
        )

    def total_drug_count(self):
        return self.conn_s.b_fetchall(
            """SELECT COUNT(*) as count
                from drug_exposure as de
                join concept as co on de.drug_concept_id=co.concept_id
                """
        )

    def total_condition(self, args):
        return self.conn_s.b_fetchall(
            """SELECT cdo.person_id ,cdo.condition_concept_id,co.concept_name as condition_source_value,
                cdo.condition_start_datetime,cdo.condition_end_datetime,cdo.visit_occurrence_id
                FROM condition_occurrence as cdo
                join concept as co on cdo.condition_concept_id=co.concept_id
                LIMIT 10 OFFSET 10 * %s""", args
        )

    def total_condition_count(self):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as count
                FROM condition_occurrence as cdo
                join concept as co on cdo.condition_concept_id=co.concept_id"""
        )

    def condition_keyword_search(self, args):
        return self.conn_s.b_fetchall(
            """SELECT cdo.person_id ,cdo.condition_concept_id,co.concept_name as condition_source_value,
                cdo.condition_start_datetime,cdo.condition_end_datetime,cdo.visit_occurrence_id
                FROM condition_occurrence as cdo
                join concept as co on cdo.condition_concept_id=co.concept_id
                WHERE co.concept_name LIKE %s
                LIMIT 10 OFFSET 10 * %s""", args
        )

    def condition_keyword_count(self, args):
        return self.conn_s.b_fetchall(
            """SELECT COUNT(*) as count
                FROM condition_occurrence as cdo
                join concept as co on cdo.condition_concept_id=co.concept_id
                WHERE co.concept_name LIKE %s
                """, args
        )
