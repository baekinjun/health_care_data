from .view import *

url_patterns = [
    (PatientTotalCount, '/patient_total_count'),
    (EachGenderCount, '/each_gender_count'),
    (EachRaceCount, '/each_race_count'),
    (EachEthnicityCount, '/each_ethnicity_count'),
    (PassAwayPersonCount, '/pass_away_person_count'),
    (VisitTypeCount, '/visit_type_count'),
    (VisitEachGenderCount, '/each_gender_visit_count'),
    (VisitEachRaceCount, '/each_race_visit_count'),
    (VisitEachEthnicityCount, '/each_ethnicity_visit_count'),
    (VisitEachGenerateCount, '/each_generate_visit_count')
]
