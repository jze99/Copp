from database import sync_engine, async_engine, sync_sassion, Base

class orm_data_functions:
    def __init__(self):
        pass
    
    def date_between(self,date_column, start, end):
        start_month, start_year = map(int, start.split('.'))
        end_month, end_year = map(int, end.split('.'))
        return (date_column >= f'{start_month}.{start_year}') & (date_column <= f'{end_month}.{end_year}')
    
    def create_user(self,tables=[]):
        with sync_sassion() as session:
            Base.metadata.drop_all(sync_engine,tables=tables)
            Base.metadata.create_all(sync_engine, tables=tables)
            session.commit()
    
    def select_data_filter(self,data_time:str, tabel:Base):
        with sync_sassion() as session:
            query = session.query(tabel).filter(tabel.data == data_time)
            result = session.execute(query)
            return result.scalars().all()
        
    def select_data(self,table:Base):
        with sync_sassion() as session:
            query = session.query(table)
            result = session.execute(query)
            return result.scalars().all()
    
    def insert_data(self,data):
        with sync_sassion() as session:
            session.add_all(data)
            session.commit()
    