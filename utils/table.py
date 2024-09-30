class Seat:
     #This is a seat
    ''' > this is a docstring
    creates object Seat
    
    '''
    def __init__(self): # gives empty string in case seat is unassigned
        self.free = True        
        self.occupant = ""
    
    def set_occupant(self,name): # in case seat is free, assign someone 
        self.free = False
        self.occupant = name
   
    def remove_occuptant(self): # removes occupant from seat > return it into empty string
        self.free = True
        self.occupant = ""

class Table: 
    # This is a table
    
    def __init__(self):
        self.capacity = 4
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self):
    #     for seat in self.seats:
    #         if seat in self.seats == True:
    #             return True
    #         else:
    #             return False
        return self.capacity - self.left_capacity() > 0

    def assign_seat(self, name):
        for seat in self.seats:
            if seat in self.seats == True:
                seat.set_occupant(name)
                break
    
    def left_capacity(self):
       sum(int(1 for self.has_free_spot in self.seats))
           
pass