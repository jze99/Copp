from queries.orm import select_data

class data_dinam:
    def 

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
    

def validate_data_or_none(data):
    if (data != 'None'):
        return data
    else:
        return 0

def load_data():
    temp = select_data()  # забираем данные из базы
    poo_dict_start = {}
    poo_dict_end = {}
    
    for t in temp:
        poo = t.poo
        date_str = t.data  # assume this is the date column
        month, year = map(int, date_str.split('.'))
        
        if month <=7 :  # separate data into two dictionaries based on the year
            if poo not in poo_dict_start:
                poo_dict_start[poo] = data_FPM_POO(
                    poo=poo,
                    summ=(int(validate_data_or_none(t.undergoing_production_practice)) + int(validate_data_or_none(t.will_undergo_production_internship)) + int(validate_data_or_none(t.employed_by_company)) + int(validate_data_or_none(t.total))),
                    undergoing_production_practice=int(validate_data_or_none(t.undergoing_production_practice)),
                    will_undergo_production_internship=int(validate_data_or_none(t.will_undergo_production_internship)),
                    employed_by_company=int(validate_data_or_none(t.employed_by_company)),
                    total=int(validate_data_or_none(t.total)),
                    data=t.data
                )
            else:
                poo_dict_start[poo].summ_data(
                    summ=(int(validate_data_or_none(t.undergoing_production_practice)) + int(validate_data_or_none(t.will_undergo_production_internship)) + int(validate_data_or_none(t.employed_by_company)) + int(validate_data_or_none(t.total))),
                    undergoing_production_practice=int(validate_data_or_none(t.undergoing_production_practice)),
                    will_undergo_production_internship=int(validate_data_or_none(t.will_undergo_production_internship)),
                    employed_by_company=int(validate_data_or_none(t.employed_by_company)),
                    total=int(validate_data_or_none(t.total))
                )
        else:
            if poo not in poo_dict_end:
                poo_dict_end[poo] = data_FPM_POO(
                    poo=poo,
                    summ=(int(validate_data_or_none(t.undergoing_production_practice)) + int(validate_data_or_none(t.will_undergo_production_internship)) + int(validate_data_or_none(t.employed_by_company)) + int(validate_data_or_none(t.total))),
                    undergoing_production_practice=int(validate_data_or_none(t.undergoing_production_practice)),
                    will_undergo_production_internship=int(validate_data_or_none(t.will_undergo_production_internship)),
                    employed_by_company=int(validate_data_or_none(t.employed_by_company)),
                    total=int(validate_data_or_none(t.total)),
                    data=t.data
                )
            else:
                poo_dict_end[poo].summ_data(
                    summ=(int(validate_data_or_none(t.undergoing_production_practice)) + int(validate_data_or_none(t.will_undergo_production_internship)) + int(validate_data_or_none(t.employed_by_company)) + int(validate_data_or_none(t.total))),
                    undergoing_production_practice=int(validate_data_or_none(t.undergoing_production_practice)),
                    will_undergo_production_internship=int(validate_data_or_none(t.will_undergo_production_internship)),
                    employed_by_company=int(validate_data_or_none(t.employed_by_company)),
                    total=int(validate_data_or_none(t.total))
                )
    
    return [poo_dict_start, poo_dict_end]
