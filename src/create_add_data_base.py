import os
import sys
sys.path.insert(1,os.path.join(sys.path[0],'..'))

from queries.orm import create_user,insert_data, read_xlsx_file
from models import FPM_POO_orm

#
#create_user()
def test():
    test_mass=[]
    xlsx=read_xlsx_file("ОПК РАБОЧИЙ (июль 2024).xlsx")
    for ixl,xl in enumerate(xlsx):
        if ixl == 0:
            continue
        test=FPM_POO_orm(
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
        test_mass.append(test)
        
    return test_mass
        
insert_data(test())