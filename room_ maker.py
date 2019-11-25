
import random
from room import Room
# build room
# border on walls

room_number = random.randint(3,5)
def place_player(current_room = Room(),player_row = 0,player_index = 0):
    
    current_layout = current_room.layout
    
    
    if player_row != 0 and player_index != 0:
        
        current_layout[player_row][player_index]
        
        
    else:
        
        if len(current_layout) == 3:
        
            spawn_row = current_layout[1]
            
        else:
            
            row_median = len(current_layout) // 2
        
        
       
           
           
        
        
        
        
        
'''
def build_room():

    length = 
    width = random.randint(3,20)

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
            
            
    return room
    
'''

def place_door(room, room_total):

     
    layout = room.layout
    length = room.length
    width = room.width
    room_num = room.room_num
    
    if room_num == 1 or room_num == room_total:
    
        door_row = random.randint(0,length-1)

        if door_row == 0 or door_row == (length-1):
    
            door_index = random.randint(1, (width-2))
        
            layout[door_row][door_index] = 'd'
    
        else:
    
            door_side = random.randint(0,1)
    
            if door_side == 0:
        
                layout[door_row][0]  = 'd'
        
            elif door_side == 1:
        
                layout[door_row][-1] = 'd'
               
                
    else:
           
        last_door_row = None

        
        
        for n in range(2):
            
            door_row = random.randint(0,length-1)
            
            while last_door_row  and last_door_row == door_row:
                
                door_row = random.randint(0,length-1)
                
                
            if door_row == 0 or door_row == (length-1):
        
                door_index = random.randint(1, (width-2))
                        
                layout[door_row][door_index] = 'd' 
                
            else:
    
                door_side = random.randint(0,1)
    
                if door_side == 0:
                    
                    door_index = 0
                    layout[door_row][door_index]  = 'd'
        
                elif door_side == 1:
                    
                    door_index = -1
                    layout[door_row][door_index] = 'd'
                    
                    
            last_door_row = door_row
            
                    
                    
                    
                
 
def print_room(room):
    
    for row in room:
    
        s = ""
    
        d = s.join(row)
    
        print(d)
        
        
        
    
def main():
    
    
    room_total = random.randint(3,5)

    level = []

    for n in range(room_total):
        
        room = Room(room_num = (n+1))   
        place_door(room,room_total)
        
        level.append(room)
        
        
    for room in level:
        
        print_room(room.layout)

main()
        
    
    