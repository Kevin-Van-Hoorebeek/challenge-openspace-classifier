class Seat:

    def __init__(self):
        self.free = True        
        self.occupant = ""
    
    def set_occupant(self,name):
        self.free = False
        self.occupant = name
   
    def remove_occuptant(self):
        self.free = True
        self.occupant = ""

class Table:
    
    def __init__(self):
        self.capacity = 4
        self.seat = []
        for i in range(self.capacity):
           self.seats.append(Seat())

    
    def has_free_spot(self):
        
        for i in self.seat:
         if i.free == True:
            return True
         break

    def assign_seat(self, name):
        self.assign_seat = name 
    
    def left_capacity(self):
       if self.left_capacity == int(0):
        return False
       elif self.left_capacity > int(0):
        return True
        pass


        pass