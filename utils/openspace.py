import random
from table import Table


class Openspace:
    def __init__(self, tables, number_of_tables):
        self.tables = tables
        self.number_of_tables = number_of_tables

def organize(names): # assign seats at random till seats are filled up
    random_names = random.shuffle(names)
    number_of_tables = 6
    number_of_tables_list = [Table(i) for i in range(number_of_tables)]
    random_names.assign_seat in number_of_tables_list
    return number_of_tables_list

    

def display(self): # display output
    self.display = 
    
    
    
    pass



    
