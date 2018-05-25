import random
import time
import pprint
import numpy
import copy 
'''
aList = [[1,2,3],[5,6,7]]

print(aList[0][2])

Dict = {}

Dict[0] = aList

for item in Dict.values():
    print(item)
    if item == aList:
        print('Same') 
'''

class Tree:
    pass

def log_move(str_value, direction):
    if str_value not in log.keys():
        log[str_value] = []


    if direction not in log[str_value]:
        log[str_value].append(direction)


    print('logging',grid_id)
    
def create_grid():
    global size
    global zero_x
    global zero_y
    grid = []
    acceptable_size = False

    
    while acceptable_size != True:
        #Asking For Size Of Grid Row and Column = Size
        size = int(input('Enter the length of the grid\n'))
        if size > 1:
            acceptable_size = True
            
    numbers = list(range(0,size ** 2)) #Create a random list of numbers between 0 to size**2 (will not include last number e.g 5**2 = 25 but numbers will be from 0 - 24
    
    for y in range(size):
        grid.append([])#creates row
        for x in range(size):
            value = random.choice(numbers) #randomly picks a value from numbers list
            if value == 0:
                zero_x = x #tracks where Zero is
                zero_y = y
            grid[y].append(value) #Adds the value into the row
            numbers.remove(value)
    
            
    print('The Starting Grid Is:')
    #prints grid
    for row in grid:
        print(row)
    print(grid)
    print('With Zero lying on the point', '(' + str(zero_x) + ',' + str(zero_y) + ')')

    return grid

def str_value(grid):
    grid1d = []
    str_grid = None
    for row in grid:
        for column in row:
            grid1d.append(str(column))

    str_grid = ''.join(grid1d)

    return str_grid
    
def grid_connections(parent,child):
    #takes the parent and child grids and converts then into a str format
    parent_str = str_value(parent)
    
    child_str = str_value(child)
    
    if parent_str not in connections.keys():
        connections[parent_str] = []

    if child_str not in connections[parent_str]:
        connections[parent_str].append(child_str)

    
def target():
    #fills the grid from 0 - (size**2 - 1)
    perfect_grid = []
    numbers = list(range(0, size**2))
    
    for y in range(size):
        perfect_grid.append([])
        for x in range(size):
            perfect_grid[y].append(numbers.pop(0))

def unique_grid(grid):
    global grid_id
    global grid_key
    unique = False
    
    str_grid = str_value(grid)
    
    if str_grid not in grid_key.values():
        unique = True
        grid_id += 1
        grid_key[grid_id] = str_grid

    if str_grid == '012345678':
        pprint.pprint(grid_key)
        time.sleep(10000000000000)
        
        
    return unique

def backtrack(grid):
    global zero_x
    global zero_y
    global back_grid
    
    print('prev', grid)
    
    count = 1
    grid_loc = None
    
    while not grid_loc:
        print('RUNNING LOOP')
        if grid_key[grid_id - count] in backtracked:
            count += 1
        else:
            grid_loc = grid_key[grid_id - count]

    #takes the previous grid
    temp_list = [[] for i in range(size)] #converts it into a 2d array
    print (" -> backtrack" , grid_loc, temp_list); 
    
    for x in range(size):
        value = grid_loc[size*x:size*(x+1)]
        
        for char in value:
            temp_list[x].append(int(char))
        

    #finds where 0 is


    for y in range(size):
        for x in range(size):
            if temp_list[y][x] == 0:
                zero_x = x
                zero_y = y
                
    print('Backtracking')
    print(str_value(temp_list))
    #move(temp_list)
    print ("<- backtrack");
    backtracked.append(str_value(grid))
    back_grid = temp_list
    
    return temp_list
    
def move(grid):
    print ("-> MOVE" , grid);

    global zero_x
    global zero_y
    print('==========')
    #Creates a deepcopy of where zero is incase no change in the move is made
    p_x,p_y = copy.deepcopy(zero_x), copy.deepcopy(zero_y)
    
    x,y = zero_x, zero_y
    #Grid put into temp_grid for manipulation and verifying if its a new unique grid
    temp_grid = copy.deepcopy(grid)

    moves = ['U','D','L','R']

    #If the value is in the first column you can't move left
    if x == 0:
        moves.remove('L')
    #If the value is in the top row you can't move up
    if y == 0:
        moves.remove('U')
    #If the value is in the last column you can't move right
    if x == (size - 1):
        moves.remove('R')
    #If the value is in the bottom row you can't move down
    if y == (size - 1):
        moves.remove('D')

    print(moves)
    #If the value has previous logged moves they will be removed from the moves list
    if str_value(temp_grid) in log.keys():
        print('removing moves')
        for aMove in log[str_value(temp_grid)]:
            if aMove in moves:
                print('Moves:', moves)
                moves.remove(aMove)
                
    print(moves)

    #If there are no moves available the previous node will be used to see if it has any available moves
    if len(moves) == 0:
        move(backtrack(temp_grid))
        grid = back_grid
        print('backtrack grid',grid)



    #print(len(moves))
       # print(direction)
    
    else:
        #Moves the zero around according to what move was selected
        direction = random.choice(moves)

        if direction == 'U':
            
            swap = temp_grid[y-1][x] #holds the value that is going to be swapped with zero
            temp_grid[y-1][x] = 0
            temp_grid[y][x] = swap
            zero_y = zero_y - 1 
            
        if direction == 'D':
            swap = temp_grid[y+1][x] #holds the value that is going to be swapped with zero
            temp_grid[y+1][x] = 0
            temp_grid[y][x] = swap
            zero_y = zero_y + 1         
            
        if direction == 'L':
            swap = temp_grid[y][x-1] #holds the value that is going to be swapped with zero
            temp_grid[y][x-1] = 0
            temp_grid[y][x] = swap
            zero_x = zero_x - 1
            
        if direction == 'R':
            swap = temp_grid[y][x+1] #holds the value that is going to be swapped with zero
            temp_grid[y][x+1] = 0
            temp_grid[y][x] = swap
            zero_x = zero_x + 1

        unique = unique_grid(temp_grid) #Returns if the grid is unique or not

        if unique == True:
            log_move(str_value(temp_grid), direction) #move is logged
            grid_connections(grid,temp_grid) #connection added
            grid = temp_grid
            
        if unique == False:
            print('not unique')
            log_move(str_value(grid), direction)
            zero_x, zero_y = p_x, p_y

        print(moves)
        print(grid)
        print('<- Move');
        print('---------')
    return grid

def create_tree():
    global grid_key
    global grid_id
    global log
    global connections
    global backtracked
    
    grid = create_grid()
    backtracked = []
    goal = target()
    grid_key = {} #records grid_id and the str_grid itself
    connections = {} #records parent and children
    log = {} #records the grid and the moves it has made
    #This is purely for converting the 2d array into a string format so it is easier to compare two grids with each other
    grid_id = 0
    grid1d = []
    str_grid = None
    for row in grid:
        for column in row:
            grid1d.append(str(column))

    str_grid = ''.join(grid1d)

    print(str_grid)
            
            
    grid_key[grid_id] = str_grid

    start_grid = grid
    
    goal_reached = False

    while goal_reached != True:
        print('grid returned',grid)
        grid = move(grid)
    
def main():
    create_tree()


main()
