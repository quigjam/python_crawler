import random

class Room:
    
            

    
    
    def __init__(self,length_floor = 3, length_ceiling = 20, width_floor = 3, width_ceiling = 20, room_num = 1, level_num = 1):
        
        self.length = random.randint(length_floor, length_ceiling)
 
        self.width  = random.randint(width_floor, width_ceiling)
        
        self.room_num  = room_num
        self.level_num = level_num
        
        
        
        room = []

        for n in range(self.length):
    

            if n == 0 or n == (self.length-1):
                row = ['-'] * self.width
    
                room.append(row)
        
            else:
    
                row = ['.'] * self.width
        
                row[0]  = '|'
                row[-1] = '|'
    
                room.append(row)
                
                
        
        
        self.layout = room
        

    '''     
    def build_room(length,width):
    
        length = self.length
        width = self.width
        
        print(length)
        print(width)

        room = []

        for n in range(length):
    

            if n == 0 or n == (length-1):
                row = ['-'] * width
    
                room.append(row)
        
            else:
    
                row = ['.'] * width
        
                row[0]  = '|'
                row[-1] = '|'
    
                room.append(row)
                
        self.layout = room
        
    '''
        
    def __str__(self):
        
        for row in self.layout:
    
            s = ""
    
            d = s.join(row)
    
            return(d)
        


