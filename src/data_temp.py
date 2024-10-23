from src.queries.orm import orm_data_functions
from src.models import Data_employment_orm, Employment_orm,Data_FPM_POO_orm,FPM_POO_orm

class data_dynamics:
    def __init__(self,summ:int,undergoing_production_practice:int,will_undergo_production_internship:int,employed_by_company:int,total:int,data:str):
        self.summ:int=summ
        self.undergoing_production_practice:int=undergoing_production_practice
        self.will_undergo_production_internship:int=will_undergo_production_internship
        self.employed_by_company:int=employed_by_company
        self.total:int =total
        self.data:str=data
    
    def summ_data(self,summ:int,undergoing_production_practice:int,will_undergo_production_internship:int,employed_by_company:int,total:int):
        self.summ+=summ
        self.undergoing_production_practice+=undergoing_production_practice
        self.will_undergo_production_internship+=will_undergo_production_internship
        self.employed_by_company+=employed_by_company
        self.total+=total

class data_FPM_POO:
    
    def __init__(self,poo:str,summ:int,undergoing_production_practice:int,will_undergo_production_internship:int,employed_by_company:int,total:int,data:str):
        self.poo:str=poo
        self.summ:int=summ
        self.undergoing_production_practice:int=undergoing_production_practice
        self.will_undergo_production_internship:int=will_undergo_production_internship
        self.employed_by_company:int=employed_by_company
        self.total:int =total
        self.data:str=data
    
    def get_poo(self):
        temp = self.poo
        return temp
     
    def summ_data(self,summ:int,undergoing_production_practice:int,will_undergo_production_internship:int,employed_by_company:int,total:int):
        self.summ+=summ
        self.undergoing_production_practice+=undergoing_production_practice
        self.will_undergo_production_internship+=will_undergo_production_internship
        self.employed_by_company+=employed_by_company
        self.total+=total
    
    def sort_poo(self):
        pass
    
class data_FPM_dinamics(orm_data_functions):
    def __init__(self, data):
        self.poo_data_time_filter={}
        self.model_data={}
        self.poo_dinamics={}
        self.data = data
    
    def validate_data_or_none(self,data):
        if (data != 'None'):
            return data
        else:
            return 0
     
    def load_data(self): 
        #temp_data = self.select_data(table=Data_FPM_POO_orm)
        for data in self.data:
            self.poo_data_time_filter[data] = self.select_data_filter(data_time=data, tabel=FPM_POO_orm)  
        self.filter_data()
       
    def filter_data(self):
        for data in self.poo_data_time_filter:
            self.model_data[data] = self.create_model_data_poo(data=data)
            self.poo_dinamics[data] = self.crate_model_data_dinamic(data=data)
        pass
            
    def create_model_data_poo(self, data):
        model_data_poo={}    
        for model in self.poo_data_time_filter[data]:
            if model.poo not in model_data_poo:
                model_data_poo[model.poo] = data_FPM_POO(
                    poo=model.poo,
                    summ=(int(self.validate_data_or_none(model.undergoing_production_practice)) + int(self.validate_data_or_none(model.will_undergo_production_internship)) + int(self.validate_data_or_none(model.employed_by_company)) + int(self.validate_data_or_none(model.total))),
                    undergoing_production_practice=int(self.validate_data_or_none(model.undergoing_production_practice)),
                    will_undergo_production_internship=int(self.validate_data_or_none(model.will_undergo_production_internship)),
                    employed_by_company=int(self.validate_data_or_none(model.employed_by_company)),
                    total=int(self.validate_data_or_none(model.total)),
                    data=model.data
                )
            else:
                model_data_poo[model.poo].summ_data(
                    summ=(int(self.validate_data_or_none(model.undergoing_production_practice)) + int(self.validate_data_or_none(model.will_undergo_production_internship)) + int(self.validate_data_or_none(model.employed_by_company)) + int(self.validate_data_or_none(model.total))),
                    undergoing_production_practice=int(self.validate_data_or_none(model.undergoing_production_practice)),
                    will_undergo_production_internship=int(self.validate_data_or_none(model.will_undergo_production_internship)),
                    employed_by_company=int(self.validate_data_or_none(model.employed_by_company)),
                    total=int(self.validate_data_or_none(model.total)),
                )
        return model_data_poo
    
    def crate_model_data_dinamic(self,data):   
        model_data_poo={}
        for model in self.poo_data_time_filter[data]:
            if data not in model_data_poo:
                model_data_poo[data] = data_dynamics(
                    summ=(int(self.validate_data_or_none(model.undergoing_production_practice)) + int(self.validate_data_or_none(model.will_undergo_production_internship)) + int(self.validate_data_or_none(model.employed_by_company)) + int(self.validate_data_or_none(model.total))),
                    undergoing_production_practice=int(self.validate_data_or_none(model.undergoing_production_practice)),
                    will_undergo_production_internship=int(self.validate_data_or_none(model.will_undergo_production_internship)),
                    employed_by_company=int(self.validate_data_or_none(model.employed_by_company)),
                    total=int(self.validate_data_or_none(model.total)),
                    data=model.data
                )
            else:
                model_data_poo[data].summ_data(
                    summ=(int(self.validate_data_or_none(model.undergoing_production_practice)) + int(self.validate_data_or_none(model.will_undergo_production_internship)) + int(self.validate_data_or_none(model.employed_by_company)) + int(self.validate_data_or_none(model.total))),
                    undergoing_production_practice=int(self.validate_data_or_none(model.undergoing_production_practice)),
                    will_undergo_production_internship=int(self.validate_data_or_none(model.will_undergo_production_internship)),
                    employed_by_company=int(self.validate_data_or_none(model.employed_by_company)),
                    total=int(self.validate_data_or_none(model.total))
                )
        mode_ret = []
        for mode in model_data_poo:
            mode_ret.append(model_data_poo[mode])
        return mode_ret

class spec_data_employment:
    def __init__(
            self,
            The_total_output,
            Employed,
            of_these_employed_in_their_profession_specialty,
            Registered_as_an_individual_entrepreneur_or_self_employed,
            They_will_be_employed,
            of_these_they_will_be_employed_in_their_profession_specialty,
            They_plan_to_register_as_an_individual,
            They_have_continued_their_studies_and_have_not_found_a_job,
            Drafted_into_the_Armed_Forces_of_the_Russian_Federation,
            Are_on_parental_leave,
            They_are_under_investigation_and_are_serving_their_sentence,
            They_take_care_of_sick_relatives,
            Registered_in_employment_centers_as_unemployed,
            Have_moved_outside_the_Russian_Federation,
            They_do_not_plan_to_get_a_job_including,
            Severe_health_condition_that_does_not_allow_employment_death,
            Other_reasons_for_being_at_risk_of_disability
        ):
        self.The_total_output=The_total_output
        self.Employed=Employed
        self.of_these_employed_in_their_profession_specialty=of_these_employed_in_their_profession_specialty
        self.Registered_as_an_individual_entrepreneur_or_self_employed=Registered_as_an_individual_entrepreneur_or_self_employed
        self.They_will_be_employed=They_will_be_employed
        self.of_these_they_will_be_employed_in_their_profession_specialty=of_these_they_will_be_employed_in_their_profession_specialty
        self.They_plan_to_register_as_an_individual=They_plan_to_register_as_an_individual
        self.They_have_continued_their_studies_and_have_not_found_a_job=They_have_continued_their_studies_and_have_not_found_a_job
        self.Drafted_into_the_Armed_Forces_of_the_Russian_Federation=Drafted_into_the_Armed_Forces_of_the_Russian_Federation
        self.Are_on_parental_leave=Are_on_parental_leave
        self.They_are_under_investigation_and_are_serving_their_sentence=They_are_under_investigation_and_are_serving_their_sentence
        self.They_take_care_of_sick_relatives=They_take_care_of_sick_relatives
        self.Registered_in_employment_centers_as_unemployed=Registered_in_employment_centers_as_unemployed
        self.Have_moved_outside_the_Russian_Federation=Have_moved_outside_the_Russian_Federation
        self.They_do_not_plan_to_get_a_job_including=They_do_not_plan_to_get_a_job_including
        self.Severe_health_condition_that_does_not_allow_employment_death=Severe_health_condition_that_does_not_allow_employment_death
        self.Other_reasons_for_being_at_risk_of_disability=Other_reasons_for_being_at_risk_of_disability

    def add_data(
            self,
            The_total_output,
            Employed,
            of_these_employed_in_their_profession_specialty,
            Registered_as_an_individual_entrepreneur_or_self_employed,
            They_will_be_employed,
            of_these_they_will_be_employed_in_their_profession_specialty,
            They_plan_to_register_as_an_individual,
            They_have_continued_their_studies_and_have_not_found_a_job,
            Drafted_into_the_Armed_Forces_of_the_Russian_Federation,
            Are_on_parental_leave,
            They_are_under_investigation_and_are_serving_their_sentence,
            They_take_care_of_sick_relatives,
            Registered_in_employment_centers_as_unemployed,
            Have_moved_outside_the_Russian_Federation,
            They_do_not_plan_to_get_a_job_including,
            Severe_health_condition_that_does_not_allow_employment_death,
            Other_reasons_for_being_at_risk_of_disability
        ):
        self.The_total_output+=The_total_output
        self.Employed+=Employed
        self.of_these_employed_in_their_profession_specialty+=of_these_employed_in_their_profession_specialty
        self.Registered_as_an_individual_entrepreneur_or_self_employed+=Registered_as_an_individual_entrepreneur_or_self_employed
        self.They_will_be_employed+=They_will_be_employed
        self.of_these_they_will_be_employed_in_their_profession_specialty+=of_these_they_will_be_employed_in_their_profession_specialty
        self.They_plan_to_register_as_an_individual+=They_plan_to_register_as_an_individual
        self.They_have_continued_their_studies_and_have_not_found_a_job+=They_have_continued_their_studies_and_have_not_found_a_job
        self.Drafted_into_the_Armed_Forces_of_the_Russian_Federation+=Drafted_into_the_Armed_Forces_of_the_Russian_Federation
        self.Are_on_parental_leave+=Are_on_parental_leave
        self.They_are_under_investigation_and_are_serving_their_sentence+=They_are_under_investigation_and_are_serving_their_sentence
        self.They_take_care_of_sick_relatives+=They_take_care_of_sick_relatives
        self.Registered_in_employment_centers_as_unemployed+=Registered_in_employment_centers_as_unemployed
        self.Have_moved_outside_the_Russian_Federation+=Have_moved_outside_the_Russian_Federation
        self.They_do_not_plan_to_get_a_job_including+=They_do_not_plan_to_get_a_job_including
        self.Severe_health_condition_that_does_not_allow_employment_death+=Severe_health_condition_that_does_not_allow_employment_death
        self.Other_reasons_for_being_at_risk_of_disability+=Other_reasons_for_being_at_risk_of_disability
    
class data_employment:
    def __init__(
            self,
            The_total_output,
            Employed,
            of_these_employed_in_their_profession_specialty,
            Registered_as_an_individual_entrepreneur_or_self_employed,
            They_will_be_employed,
            of_these_they_will_be_employed_in_their_profession_specialty,
            They_plan_to_register_as_an_individual,
            They_have_continued_their_studies_and_have_not_found_a_job,
            Drafted_into_the_Armed_Forces_of_the_Russian_Federation,
            Are_on_parental_leave,
            They_are_under_investigation_and_are_serving_their_sentence,
            They_take_care_of_sick_relatives,
            Registered_in_employment_centers_as_unemployed,
            Have_moved_outside_the_Russian_Federation,
            They_do_not_plan_to_get_a_job_including,
            Severe_health_condition_that_does_not_allow_employment_death,
            Other_reasons_for_being_at_risk_of_disability
        ):
        self.The_total_output=The_total_output
        self.Employed=Employed
        self.of_these_employed_in_their_profession_specialty=of_these_employed_in_their_profession_specialty
        self.Registered_as_an_individual_entrepreneur_or_self_employed=Registered_as_an_individual_entrepreneur_or_self_employed
        self.They_will_be_employed=They_will_be_employed
        self.of_these_they_will_be_employed_in_their_profession_specialty=of_these_they_will_be_employed_in_their_profession_specialty
        self.They_plan_to_register_as_an_individual=They_plan_to_register_as_an_individual
        self.They_have_continued_their_studies_and_have_not_found_a_job=They_have_continued_their_studies_and_have_not_found_a_job
        self.Drafted_into_the_Armed_Forces_of_the_Russian_Federation=Drafted_into_the_Armed_Forces_of_the_Russian_Federation
        self.Are_on_parental_leave=Are_on_parental_leave
        self.They_are_under_investigation_and_are_serving_their_sentence=They_are_under_investigation_and_are_serving_their_sentence
        self.They_take_care_of_sick_relatives=They_take_care_of_sick_relatives
        self.Registered_in_employment_centers_as_unemployed=Registered_in_employment_centers_as_unemployed
        self.Have_moved_outside_the_Russian_Federation=Have_moved_outside_the_Russian_Federation
        self.They_do_not_plan_to_get_a_job_including=They_do_not_plan_to_get_a_job_including
        self.Severe_health_condition_that_does_not_allow_employment_death=Severe_health_condition_that_does_not_allow_employment_death
        self.Other_reasons_for_being_at_risk_of_disability=Other_reasons_for_being_at_risk_of_disability

    def add_data(
            self,
            The_total_output,
            Employed,
            of_these_employed_in_their_profession_specialty,
            Registered_as_an_individual_entrepreneur_or_self_employed,
            They_will_be_employed,
            of_these_they_will_be_employed_in_their_profession_specialty,
            They_plan_to_register_as_an_individual,
            They_have_continued_their_studies_and_have_not_found_a_job,
            Drafted_into_the_Armed_Forces_of_the_Russian_Federation,
            Are_on_parental_leave,
            They_are_under_investigation_and_are_serving_their_sentence,
            They_take_care_of_sick_relatives,
            Registered_in_employment_centers_as_unemployed,
            Have_moved_outside_the_Russian_Federation,
            They_do_not_plan_to_get_a_job_including,
            Severe_health_condition_that_does_not_allow_employment_death,
            Other_reasons_for_being_at_risk_of_disability
        ):
        self.The_total_output+=The_total_output
        self.Employed+=Employed
        self.of_these_employed_in_their_profession_specialty+=of_these_employed_in_their_profession_specialty
        self.Registered_as_an_individual_entrepreneur_or_self_employed+=Registered_as_an_individual_entrepreneur_or_self_employed
        self.They_will_be_employed+=They_will_be_employed
        self.of_these_they_will_be_employed_in_their_profession_specialty+=of_these_they_will_be_employed_in_their_profession_specialty
        self.They_plan_to_register_as_an_individual+=They_plan_to_register_as_an_individual
        self.They_have_continued_their_studies_and_have_not_found_a_job+=They_have_continued_their_studies_and_have_not_found_a_job
        self.Drafted_into_the_Armed_Forces_of_the_Russian_Federation+=Drafted_into_the_Armed_Forces_of_the_Russian_Federation
        self.Are_on_parental_leave+=Are_on_parental_leave
        self.They_are_under_investigation_and_are_serving_their_sentence+=They_are_under_investigation_and_are_serving_their_sentence
        self.They_take_care_of_sick_relatives+=They_take_care_of_sick_relatives
        self.Registered_in_employment_centers_as_unemployed+=Registered_in_employment_centers_as_unemployed
        self.Have_moved_outside_the_Russian_Federation+=Have_moved_outside_the_Russian_Federation
        self.They_do_not_plan_to_get_a_job_including+=They_do_not_plan_to_get_a_job_including
        self.Severe_health_condition_that_does_not_allow_employment_death+=Severe_health_condition_that_does_not_allow_employment_death
        self.Other_reasons_for_being_at_risk_of_disability+=Other_reasons_for_being_at_risk_of_disability
    
class data_employment_dynamics(orm_data_functions):
    def __init__(self, data):
        self.data_sort_base={}
        self.data_sort_spec={}
        self.data_other_denamic={}
        self.data_spec_data={}
        self.data=data
        
    def add_sort_spech(self, data, object):
        if object.The_code_and_name_of_the_profession_specialty not in self.data_sort_spec:
            self.data_sort_spec[object.The_code_and_name_of_the_profession_specialty] = spec_data_employment(
                The_total_output=int(object.The_total_output),
                Employed=int(object.Employed),
                of_these_employed_in_their_profession_specialty=int(object.of_these_employed_in_their_profession_specialty),
                Registered_as_an_individual_entrepreneur_or_self_employed=int(object.Registered_as_an_individual_entrepreneur_or_self_employed),
                They_will_be_employed=int(object.They_will_be_employed),
                of_these_they_will_be_employed_in_their_profession_specialty=int(object.of_these_they_will_be_employed_in_their_profession_specialty),
                They_plan_to_register_as_an_individual=int(object.They_plan_to_register_as_an_individual),
                They_have_continued_their_studies_and_have_not_found_a_job=int(object.They_have_continued_their_studies_and_have_not_found_a_job),
                Drafted_into_the_Armed_Forces_of_the_Russian_Federation=int(object.Drafted_into_the_Armed_Forces_of_the_Russian_Federation),
                Are_on_parental_leave=int(object.Are_on_parental_leave),
                They_are_under_investigation_and_are_serving_their_sentence=int(object.They_are_under_investigation_and_are_serving_their_sentence),
                They_take_care_of_sick_relatives=int(object.They_take_care_of_sick_relatives),
                Registered_in_employment_centers_as_unemployed=int(object.Registered_in_employment_centers_as_unemployed),
                Have_moved_outside_the_Russian_Federation=int(object.Have_moved_outside_the_Russian_Federation),
                They_do_not_plan_to_get_a_job_including=int(object.They_do_not_plan_to_get_a_job_including),
                Severe_health_condition_that_does_not_allow_employment_death=int(object.Severe_health_condition_that_does_not_allow_employment_death),
                Other_reasons_for_being_at_risk_of_disability=int(object.Other_reasons_for_being_at_risk_of_disability)
            )
        else:
            self.data_sort_spec[object.The_code_and_name_of_the_profession_specialty].add_data(
                The_total_output=int(object.The_total_output),
                Employed=int(object.Employed),
                of_these_employed_in_their_profession_specialty=int(object.of_these_employed_in_their_profession_specialty),
                Registered_as_an_individual_entrepreneur_or_self_employed=int(object.Registered_as_an_individual_entrepreneur_or_self_employed),
                They_will_be_employed=int(object.They_will_be_employed),
                of_these_they_will_be_employed_in_their_profession_specialty=int(object.of_these_they_will_be_employed_in_their_profession_specialty),
                They_plan_to_register_as_an_individual=int(object.They_plan_to_register_as_an_individual),
                They_have_continued_their_studies_and_have_not_found_a_job=int(object.They_have_continued_their_studies_and_have_not_found_a_job),
                Drafted_into_the_Armed_Forces_of_the_Russian_Federation=int(object.Drafted_into_the_Armed_Forces_of_the_Russian_Federation),
                Are_on_parental_leave=int(object.Are_on_parental_leave),
                They_are_under_investigation_and_are_serving_their_sentence=int(object.They_are_under_investigation_and_are_serving_their_sentence),
                They_take_care_of_sick_relatives=int(object.They_take_care_of_sick_relatives),
                Registered_in_employment_centers_as_unemployed=int(object.Registered_in_employment_centers_as_unemployed),
                Have_moved_outside_the_Russian_Federation=int(object.Have_moved_outside_the_Russian_Federation),
                They_do_not_plan_to_get_a_job_including=int(object.They_do_not_plan_to_get_a_job_including),
                Severe_health_condition_that_does_not_allow_employment_death=int(object.Severe_health_condition_that_does_not_allow_employment_death),
                Other_reasons_for_being_at_risk_of_disability=int(object.Other_reasons_for_being_at_risk_of_disability)
            )
        
    def add_sort_data(self,data,object):
        if data not in self.data_other_denamic:
            self.data_other_denamic[data] = data_employment(
                The_total_output=int(object.The_total_output),
                Employed=int(object.Employed),
                of_these_employed_in_their_profession_specialty=int(object.of_these_employed_in_their_profession_specialty),
                Registered_as_an_individual_entrepreneur_or_self_employed=int(object.Registered_as_an_individual_entrepreneur_or_self_employed),
                They_will_be_employed=int(object.They_will_be_employed),
                of_these_they_will_be_employed_in_their_profession_specialty=int(object.of_these_they_will_be_employed_in_their_profession_specialty),
                They_plan_to_register_as_an_individual=int(object.They_plan_to_register_as_an_individual),
                They_have_continued_their_studies_and_have_not_found_a_job=int(object.They_have_continued_their_studies_and_have_not_found_a_job),
                Drafted_into_the_Armed_Forces_of_the_Russian_Federation=int(object.Drafted_into_the_Armed_Forces_of_the_Russian_Federation),
                Are_on_parental_leave=int(object.Are_on_parental_leave),
                They_are_under_investigation_and_are_serving_their_sentence=int(object.They_are_under_investigation_and_are_serving_their_sentence),
                They_take_care_of_sick_relatives=int(object.They_take_care_of_sick_relatives),
                Registered_in_employment_centers_as_unemployed=int(object.Registered_in_employment_centers_as_unemployed),
                Have_moved_outside_the_Russian_Federation=int(object.Have_moved_outside_the_Russian_Federation),
                They_do_not_plan_to_get_a_job_including=int(object.They_do_not_plan_to_get_a_job_including),
                Severe_health_condition_that_does_not_allow_employment_death=int(object.Severe_health_condition_that_does_not_allow_employment_death),
                Other_reasons_for_being_at_risk_of_disability=int(object.Other_reasons_for_being_at_risk_of_disability)
            )
        else:
            self.data_other_denamic[data].add_data(
                The_total_output=int(object.The_total_output),
                Employed=int(object.Employed),
                of_these_employed_in_their_profession_specialty=int(object.of_these_employed_in_their_profession_specialty),
                Registered_as_an_individual_entrepreneur_or_self_employed=int(object.Registered_as_an_individual_entrepreneur_or_self_employed),
                They_will_be_employed=int(object.They_will_be_employed),
                of_these_they_will_be_employed_in_their_profession_specialty=int(object.of_these_they_will_be_employed_in_their_profession_specialty),
                They_plan_to_register_as_an_individual=int(object.They_plan_to_register_as_an_individual),
                They_have_continued_their_studies_and_have_not_found_a_job=int(object.They_have_continued_their_studies_and_have_not_found_a_job),
                Drafted_into_the_Armed_Forces_of_the_Russian_Federation=int(object.Drafted_into_the_Armed_Forces_of_the_Russian_Federation),
                Are_on_parental_leave=int(object.Are_on_parental_leave),
                They_are_under_investigation_and_are_serving_their_sentence=int(object.They_are_under_investigation_and_are_serving_their_sentence),
                They_take_care_of_sick_relatives=int(object.They_take_care_of_sick_relatives),
                Registered_in_employment_centers_as_unemployed=int(object.Registered_in_employment_centers_as_unemployed),
                Have_moved_outside_the_Russian_Federation=int(object.Have_moved_outside_the_Russian_Federation),
                They_do_not_plan_to_get_a_job_including=int(object.They_do_not_plan_to_get_a_job_including),
                Severe_health_condition_that_does_not_allow_employment_death=int(object.Severe_health_condition_that_does_not_allow_employment_death),
                Other_reasons_for_being_at_risk_of_disability=int(object.Other_reasons_for_being_at_risk_of_disability)
            )
    
    def load_data(self):
        for row_temp_data in self.data:
            self.data_sort_base[row_temp_data] = self.select_data_filter(row_temp_data, Employment_orm)
        for data in self.data_sort_base:
            
            for object in self.data_sort_base[data]:
                self.add_sort_spech(data,object)
                self.add_sort_data(data,object)
                
            self.data_spec_data[data]=self.data_sort_spec
            
            
