from sqlalchemy import Table, Column, Integer, ForeignKey,Index,ForeignKeyConstraint, MetaData, String,PrimaryKeyConstraint,UniqueConstraint,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from typing import Optional, Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]

metadata_obj = MetaData()

class Poo_orm(Base):
    __tablename__ = "ПОО"
    id:Mapped[intpk]
    name: Mapped[str]

class Сompany_orm(Base):
    __tablename__ = "Предприятия"
    id:Mapped[intpk]
    name: Mapped[str]
    inn: Mapped[str]

class Professions_orm(Base):
    __tablename__ = "Професии"
    id:Mapped[intpk]
    name: Mapped[str]
    
class Positions_orm(Base):
    __tablename__ = "Должности"
    id:Mapped[intpk]
    name: Mapped[str]

class Data_FPM_POO_orm(Base):
    __tablename__="Дата ФПМ ПОО"
    id:Mapped[intpk]
    data:Mapped[str]
    
class FPM_POO_orm(Base):
    __tablename__="ФПМ ПОО"
    id:Mapped[intpk]
    poo:Mapped[str]
    subject:Mapped[str]
    inn:Mapped[str]
    company:Mapped[str]
    professions_positions:Mapped[str]
    profession_category:Mapped[str]
    professions_positions_:Mapped[str]
    name_profession:Mapped[str]
    number_of_vacancies:Mapped[str]
    undergoing_production_practice:Mapped[str]#проходят производственную ппарктику1
    will_undergo_production_internship:Mapped[str]#будут проходить практику2
    employed_by_company:Mapped[str]#устроенные в компанию3
    target:Mapped[str]#целевое
    total:Mapped[str]#всего4
    since_last_year:Mapped[str]#с прошлого года
    employed_this_year:Mapped[str]#Из них трудоустроенны выпускники этого года
    employed_previous_years:Mapped[str]#Из них трудоустроенные выпускники прошлых лет
    employed_previous_years_pre_call:Mapped[str]#Из них трудоустроенные выпускники прошлых лет завершивших службу по призыву
    closed_other_ways:Mapped[str]#Количество вакансий, закрытых иными способами
    mechanism_closing_different_way:Mapped[str]#Механизм закрытия иным способом
    data:Mapped[str]#дата

class Data_employment_orm(Base):
    __tablename__="Дата трудоустройство"
    id:Mapped[intpk]
    data:Mapped[str]
    
class Employment_orm(Base):
    __tablename__="Трудоустройство"
    id:Mapped[intpk]#0
    Name_of_the_educational_organization:Mapped[str]=mapped_column(nullable=True)#1                       
    The_code_and_name_of_the_profession_specialty:Mapped[str]#2
    The_total_output:Mapped[str]#3
    Employed:Mapped[str]#4
    of_these_employed_in_their_profession_specialty:Mapped[str]#5
    of_these_they_will_continue_their_studies:Mapped[str]#6
    in_the_field_of_education1:Mapped[str]#7
    in_the_medical_industry1:Mapped[str]#8
    in_the_service_sector_tourism1:Mapped[str]#9
    in_the_trade_sector_financial_sector_organizations1:Mapped[str]#10
    in_the_field_of_law_enforcement_and_management1:Mapped[str]#11
    in_the_media_industry1:Mapped[str]#12
    to_enterprises_of_the_military_industrial_complex1:Mapped[str]#13
    mechanical_engineering1:Mapped[str]#14
    agriculture1:Mapped[str]#15
    metallurg1:Mapped[str]#16
    railway_transport1:Mapped[str]#17
    light_industry1:Mapped[str]#18
    chemical_industry1:Mapped[str]#19
    nuclear_industry1:Mapped[str]#20
    pharmaceutical_industry1:Mapped[str]#21
    information_technology_industries1:Mapped[str]#22
    radio_electronics1:Mapped[str]#23
    fuel_and_energy_complex1:Mapped[str]#24
    transport_industry1:Mapped[str]#25
    mining_industry1:Mapped[str]#26
    branches_of_the_electrical_industry1:Mapped[str]#27
    forestry_industry1:Mapped[str]#28
    construction_industry1:Mapped[str]#29
    branches_of_the_electronic_industry1:Mapped[str]#30
    robotics_industries1:Mapped[str]#31
    in_the_field_of_art1:Mapped[str]#32
    Food_industry_paper_production_printing_rubber1:Mapped[str]#33
    Registered_as_an_individual_entrepreneur_or_self_employed:Mapped[str]#34
    They_will_be_employed:Mapped[str]#35
    of_these_they_will_be_employed_in_their_profession_specialty:Mapped[str]#36    
    of_them_they_will_continue_their_studies:Mapped[str]#37
    in_the_field_of_education2:Mapped[str]#38
    in_the_medical_industry2:Mapped[str]#39
    in_the_service_sector_tourism2:Mapped[str]#40
    in_the_trade_sector_financial_sector_organizations2:Mapped[str]#41
    in_the_field_of_law_enforcement_and_management2:Mapped[str]#42
    in_the_media_industry2:Mapped[str]#43
    to_enterprises_of_the_military_industrial_complex2:Mapped[str]#44
    mechanical_engineering2:Mapped[str]#45
    agriculture2:Mapped[str]#46
    metallurg2:Mapped[str]#47
    railway_transport2:Mapped[str]#48
    light_industry2:Mapped[str]#49
    chemical_industry2:Mapped[str]#50
    nuclear_industry2:Mapped[str]#51
    pharmaceutical_industry2:Mapped[str]#52
    information_technology_industries2:Mapped[str]#53
    radio_electronics2:Mapped[str]#54
    fuel_and_energy_complex2:Mapped[str]#55
    transport_industry2:Mapped[str]#56
    mining_industry2:Mapped[str]#57
    branches_of_the_electrical_industry2:Mapped[str]#58
    forestry_industry2:Mapped[str]#59
    construction_industry2:Mapped[str]#60
    branches_of_the_electronic_industry2:Mapped[str]#61
    robotics_industries2:Mapped[str]#62
    in_the_field_of_art2:Mapped[str]#63
    Food_industry_paper_production_printing_rubber2:Mapped[str]#64
    They_plan_to_register_as_an_individual:Mapped[str]#65
    They_have_continued_their_studies_and_have_not_found_a_job:Mapped[str]#66
    Drafted_into_the_Armed_Forces_of_the_Russian_Federation:Mapped[str]#67
    Are_on_parental_leave:Mapped[str]#68
    They_are_under_investigation_and_are_serving_their_sentence:Mapped[str]#69
    They_take_care_of_sick_relatives:Mapped[str]#70
    Registered_in_employment_centers_as_unemployed:Mapped[str]#71
    Have_moved_outside_the_Russian_Federation:Mapped[str]#72
    They_do_not_plan_to_get_a_job_including:Mapped[str]#73
    Severe_health_condition_that_does_not_allow_employment_death:Mapped[str]#74
    Other_reasons_for_being_at_risk_of_disability:Mapped[str]#75
    Other_reasons:Mapped[str]=mapped_column(nullable=True)#76
    Measures_taken:Mapped[str]=mapped_column(nullable=True)#77
    The_main_partner_enterprises_that_employ_graduates:Mapped[str]=mapped_column(nullable=True)#78  
    data:Mapped[str]#79                                                                                       

class User(Base):
    __tablename__ = 'users'
    id:Mapped[intpk]
    username:Mapped[str] = mapped_column(String(100), nullable=False)    
    password:Mapped[str] = mapped_column(String(200), nullable=False)
    
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username')
    )


class Post(Base):
    __tablename__ = 'posts'
    id:Mapped[intpk]
    title:Mapped[str] = mapped_column(String(100), nullable=False)
    username:Mapped[str] = mapped_column(String(200), nullable=False)
    data:Mapped[str]= mapped_column(String(100), nullable=False)
    __table_args__ = (
        ForeignKeyConstraint(['username'], ['users.username']),        
        Index('title_content_index', 'title') # composite index on title and content   
    )
