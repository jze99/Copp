import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import openpyxl
from src.models import FPM_POO_orm, Employment_orm,Data_FPM_POO_orm,Data_employment_orm
from src.queries.orm import orm_data_functions
from src.config import path_data

class validate_data(orm_data_functions):
    
    def read_xlsx_file(self,path:str,sheet:str):
        wb = openpyxl.load_workbook(path)
        sheet = wb[sheet]

        # Initialize an empty list to store the data
        data = []
        for irow, row in enumerate(sheet.iter_rows(values_only=True),start=1):
            if row[1] == None:
                continue
            data.append(list(row))
        return data
    
    def onli_data(self,data, noneble:bool=False):
        data = str(data)
        if data != 'None':
            return data
        elif noneble == False:
            return '0'
        elif noneble == True:
            return None

class craete_data_base_xlsx(validate_data):    
    
    def add_FPM_POO(self, path:str="", sheet:str=""):
        temp_mass=[]
        xlsx=self.read_xlsx_file(path=path, sheet=sheet)
        for ixl,xl in enumerate(xlsx):
            if ixl == 0 or ixl == 1:
                continue
            temp=FPM_POO_orm(
                poo=str(xl[0]),#ПОО
                subject=str(xl[1]),#Субъект РФ
                inn=str(xl[2]),#ИНН предприятия

                company=str(xl[3]),#Наименование предприятия
                professions_positions=str(xl[4]),#профессий, должностей
                professions_positions_=str(xl[5]),
                profession_category=str(xl[6]), #категория профессии, должности на предприятии

                name_profession=str(xl[7]),#Наименование профессии / специальности СПО
                number_of_vacancies=str(xl[8]),# категория профессии, должности на предприятии
                undergoing_production_practice=str(xl[9]),#Наименование профессии / специальности СПО

                will_undergo_production_internship=str(xl[10]),
                employed_by_company=str(xl[11]),
                target=str(xl[12]),

                total=str(xl[13]),
                since_last_year=str(xl[14]),
                employed_this_year=str(xl[15]),

                employed_previous_years=str(xl[16]),
                employed_previous_years_pre_call=str(xl[17]),
                closed_other_ways=str(xl[18]),

                mechanism_closing_different_way=str(xl[19]),
                data=str(xl[20])
            )
            temp_mass.append(temp)

        self.insert_data(temp_mass)
        self.insert_data(data=[Data_FPM_POO_orm(data=str(xlsx[2][20]))])
        pass
    
    def add_Employment(self, sheet:str="", path:str=""):
        temp_mass=[]
        xlsx=self.read_xlsx_file(path,sheet=sheet)
        for ixl,xl in enumerate(xlsx):
            if ixl == 0 or ixl == 1:
                continue
            temp=Employment_orm(
                Name_of_the_educational_organization=self.onli_data(xl[0],True),
                The_code_and_name_of_the_profession_specialty=self.onli_data(xl[1],True),
                The_total_output=self.onli_data(xl[2]),
                Employed=self.onli_data(xl[3]),
                of_these_employed_in_their_profession_specialty=self.onli_data(xl[4]),
                of_these_they_will_continue_their_studies=self.onli_data(xl[5]),
                in_the_field_of_education1=self.onli_data(xl[6]),
                in_the_medical_industry1=self.onli_data(xl[7]),
                in_the_service_sector_tourism1=self.onli_data(xl[8]),
                in_the_trade_sector_financial_sector_organizations1=self.onli_data(xl[9]),
                in_the_field_of_law_enforcement_and_management1=self.onli_data(xl[10]),
                in_the_media_industry1=self.onli_data(xl[11]),
                to_enterprises_of_the_military_industrial_complex1=self.onli_data(xl[12]),
                mechanical_engineering1=self.onli_data(xl[13]),
                agriculture1=self.onli_data(xl[14]),
                metallurg1=self.onli_data(xl[15]),
                railway_transport1=self.onli_data(xl[16]),
                light_industry1=self.onli_data(xl[17]),
                chemical_industry1=self.onli_data(xl[18]),
                nuclear_industry1=self.onli_data(xl[19]),
                pharmaceutical_industry1=self.onli_data(xl[20]),
                information_technology_industries1=self.onli_data(xl[21]),
                radio_electronics1=self.onli_data(xl[22]),
                fuel_and_energy_complex1=self.onli_data(xl[23]),
                transport_industry1=self.onli_data(xl[24]),
                mining_industry1=self.onli_data(xl[25]),
                branches_of_the_electrical_industry1=self.onli_data(xl[26]),
                forestry_industry1=self.onli_data(xl[27]),
                construction_industry1=self.onli_data(xl[28]),
                branches_of_the_electronic_industry1=self.onli_data(xl[29]),
                robotics_industries1=self.onli_data(xl[30]),
                in_the_field_of_art1=self.onli_data(xl[31]),
                Food_industry_paper_production_printing_rubber1=self.onli_data(xl[32]),
                Registered_as_an_individual_entrepreneur_or_self_employed=self.onli_data(xl[33]),
                They_will_be_employed=self.onli_data(xl[34]),
                of_these_they_will_be_employed_in_their_profession_specialty=self.onli_data(xl[35]),
                of_them_they_will_continue_their_studies=self.onli_data(xl[36]),
                in_the_field_of_education2=self.onli_data(xl[37]),
                in_the_medical_industry2=self.onli_data(xl[38]),
                in_the_service_sector_tourism2=self.onli_data(xl[39]),
                in_the_trade_sector_financial_sector_organizations2=self.onli_data(xl[40]),
                in_the_field_of_law_enforcement_and_management2=self.onli_data(xl[41]),
                in_the_media_industry2=self.onli_data(xl[42]),
                to_enterprises_of_the_military_industrial_complex2=self.onli_data(xl[43]),
                mechanical_engineering2=self.onli_data(xl[44]),
                agriculture2=self.onli_data(xl[45]),
                metallurg2=self.onli_data(xl[46]),
                railway_transport2=self.onli_data(xl[47]),
                light_industry2=self.onli_data(xl[48]),
                chemical_industry2=self.onli_data(xl[49]),
                nuclear_industry2=self.onli_data(xl[50]),
                pharmaceutical_industry2=self.onli_data(xl[51]),
                information_technology_industries2=self.onli_data(xl[52]),
                radio_electronics2=self.onli_data(xl[53]),
                fuel_and_energy_complex2=self.onli_data(xl[54]),
                transport_industry2=self.onli_data(xl[55]),
                mining_industry2=self.onli_data(xl[56]),
                branches_of_the_electrical_industry2=self.onli_data(xl[57]),
                forestry_industry2=self.onli_data(xl[58]),
                construction_industry2=self.onli_data(xl[59]),
                branches_of_the_electronic_industry2=self.onli_data(xl[60]),
                robotics_industries2=self.onli_data(xl[61]),
                in_the_field_of_art2=self.onli_data(xl[62]),
                Food_industry_paper_production_printing_rubber2=self.onli_data(xl[63]),
                They_plan_to_register_as_an_individual=self.onli_data(xl[64]),
                They_have_continued_their_studies_and_have_not_found_a_job=self.onli_data(xl[65]),
                Drafted_into_the_Armed_Forces_of_the_Russian_Federation=self.onli_data(xl[66]),
                Are_on_parental_leave=self.onli_data(xl[67]),
                They_are_under_investigation_and_are_serving_their_sentence=self.onli_data(xl[68]),
                They_take_care_of_sick_relatives=self.onli_data(xl[69]),
                Registered_in_employment_centers_as_unemployed=self.onli_data(xl[70]),
                Have_moved_outside_the_Russian_Federation=self.onli_data(xl[71]),
                They_do_not_plan_to_get_a_job_including=self.onli_data(xl[72]),
                Severe_health_condition_that_does_not_allow_employment_death=self.onli_data(xl[73]),
                Other_reasons_for_being_at_risk_of_disability=self.onli_data(xl[74]),
                Other_reasons=self.onli_data(xl[75],True),
                Measures_taken=self.onli_data(xl[76], True),
                The_main_partner_enterprises_that_employ_graduates=self.onli_data(xl[77],True),
                data=self.onli_data(xl[78]),
            )
            temp_mass.append(temp)

        self.insert_data(temp_mass)
        self.insert_data(data=[Data_employment_orm(data=str(xlsx[2][78]))])
    
#test = craete_data_base_xlsx()
#test.create_table([Employment_orm.__table__,Data_employment_orm.__table__])

