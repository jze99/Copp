from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from typing import Optional, Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
strnn = Annotated[str,mapped_column(nullable=False)]

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
    poo:Mapped[strnn]
    subject:Mapped[strnn]
    inn:Mapped[strnn]
    company:Mapped[strnn]
    professions_positions:Mapped[strnn]
    profession_category:Mapped[strnn]
    name_profession:Mapped[strnn]
    number_of_vacancies:Mapped[strnn]
    undergoing_production_practice:Mapped[strnn]#проходят производственную ппарктику
    will_undergo_production_internship:Mapped[strnn]#будут проходить практику
    employed_by_company:Mapped[strnn]#устроенные в компанию
    target:Mapped[strnn]#целевое
    

    
class resumes(Base):
    __tablename__ = "resume"
    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]
    compens:Mapped[Optional[int]]