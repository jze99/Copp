from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
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

    
class resumes(Base):
    __tablename__ = "resume"
    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]
    compens:Mapped[Optional[int]]