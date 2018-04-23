# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

import sys
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0]]

grid2 = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

grid1 = [[0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0]]

grid0 = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]]

goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # + o - efectivo, no puede con caminos cerrados
    #puede con mapas grandes
    # ----------------------------------------  
    value = [[99 for row in range(len(grid[col]))] for col in range(len(grid))]
    try:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    continue
                else:
                    #print([i,j])
                    init = [i,j]
                    #path_way= {}
                    open = 0
                    
                    closed = [[0 for row in range(len(grid[col]))] for col in range(len(grid))]
                    came_from = {}
                    x = init[0]
                    y = init[1]
                    g = 0
                    open = [[g,x,y]]
                    closed[init[0]][init[1]]=1
                    found = False
                    resign = False
                    while found == False and resign == False:

                        if len(open) == 0:
                            resign =True

                        else:
                            #priorityqueue
                            open.sort()
                            open.reverse()
                            next = open.pop()
                            x = next[1]
                            y = next[2]
                            g = next[0]
                            #path_way[(x,y)] = next[0]                            
                            if x == goal[0] and y== goal[1]:
                                found == True
                            else:
                                for delt in range(len(delta)):
                                    x2 = x + delta[delt][0]
                                    y2 = y + delta[delt][1]
                                    if x2 >=0 and x2< len(grid) and y2 >=0 and y2<len(grid[0]):
                                        if closed[x2][y2] == 0 and grid[x2][y2]==0:
                                            closed[x2][y2] = 1
                                            g2 = g + cost
                                            open.append([g2,x2,y2])
                                            came_from[(x2,y2)] = (x,y)                                        


                    #print(path_way)
                    #print(came_from)
                    current = (goal[0],goal[1])                        
                    start = (init[0],init[1])
                    path = [current]
                    while current != start:
                        current = came_from[current]
                        path.append(current)
                    path.reverse()

                    for step in range(len(path)):
                        weight = (len(path)-1)-step
                        value[path[step][0]][path[step][1]] = weight
                
                                            
    except Exception as e:
        pass

    print("Best pathways: ")
    for i in range(len(value)):
        print(value[i])

    return value 

compute_value(grid,goal,cost)
input()

def compute_value2(grid,goal,cost):
    #efectivo y puede con caminos cerrados
    #se rompe en mapas grandes
    
    for i in range(len(grid)):
            for j in range(len(grid[0])):
                #x_s = len(grid)    
                goal=[i,j]
                init=[0,0]
                value = [[99 for row in range(len(grid[col]))] for col in range(len(grid))]
                closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
                closed[goal[0]][goal[1]] = 1
                x = goal[0]
                y = goal[1]        
                g = 1
                #h = heuristic[x][y]
                #h = heuristic(goal,init)
                #f = g + h
                #priority Queue
                open = [[g, x, y]]
                #value[x][y] = g
                #count =0
                found = False  # flag that is set when search is complete
                resign = False # flag set if we can't find expand
                path_way = {} #costos de avance
                delta_ways ={} #señaes
                came_from = {} #camino de retorno

                while not found and not resign:
                    if len(open) == 0:
                        resign = True
                    else:
                        open.sort()
                        open.reverse()
                        next = open.pop()
                        x = next[1]
                        y = next[2]
                        g = next[0]
                        path_way[(next[1],next[2])] = next[0]
                        value[x][y] = g
                        #count +=1   
                        if x == init[0] and y == init[1]:
                            found = True
                        else:

                            for i in range(len(delta)): #este es el ciclo para aplicar el filtro de los movimientos
                                x2 = x + delta[i][0]   #actual x mas el movimiento delta(x)
                                y2 = y + delta[i][1]   #actual y mas el movimiento en delta(y)

                                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]): #filtro de delimitacion de "terreno"
                                    if closed[x2][y2] == 0 and grid[x2][y2] == 0: #verificar q no se repitan los q ya pasaron
                                        g2 = g + cost
                                        #h2 = heuristic[x2][y2]
                                        #actual = (x2,y2)
                                        #h2 = heuristic(goal,actual)
                                        #f2 = h2 + g2
                                        open.append([g2, x2, y2])
                                        closed[x2][y2] = 1 
                                        #came_from[(x2,y2)]= (x,y)  #elimina los caminos que no y los sustituye por camino correcto
                                        #delta_ways[(x,y)] = delta_name[i]
    value[len(grid)-1][len(grid[0])-1]=0
    print("Bestpathways complete: ")
    for i in range(len(value)):
        print("%s"%(value[i]))

compute_value2(grid,goal,cost)
input()

def compute_value3(grid,goal,cost):
    #no tan efectivo y puede con caminos cerrados, se rompe con mapas grandes, inverso
    
    for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = [[99 for row in range(len(grid[col]))] for col in range(len(grid))]
                x_s = len(grid)-1-i    
                y_s= len(grid[0])-1-j
                goal=[x_s,y_s]
                init=[len(grid)-1,len(grid[0])-1]
                closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
                closed[goal[0]][goal[1]] = 1
                x = goal[0]
                y = goal[1]        
                g = 1
                #h = heuristic[x][y]
                #h = heuristic(goal,init)
                #f = g + h
                #priority Queue
                open = [[g, x, y]]
                #value[x][y] = g
                #count =0
                found = False  # flag that is set when search is complete
                resign = False # flag set if we can't find expand
                path_way = {} #costos de avance
                delta_ways ={} #señaes
                came_from = {} #camino de retorno

                while not found and not resign:
                    if len(open) == 0:
                        resign = True
                    else:
                        open.sort()
                        open.reverse()
                        next = open.pop()
                        x = next[1]
                        y = next[2]
                        g = next[0]
                        path_way[(next[1],next[2])] = next[0]
                        value[x][y] = g
                        #count +=1   
                        if x == init[0] and y == init[1]:
                            found = True
                        else:

                            for i in range(len(delta)): #este es el ciclo para aplicar el filtro de los movimientos
                                x2 = x + delta[i][0]   #actual x mas el movimiento delta(x)
                                y2 = y + delta[i][1]   #actual y mas el movimiento en delta(y)

                                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]): #filtro de delimitacion de "terreno"
                                    if closed[x2][y2] == 0 and grid[x2][y2] == 0: #verificar q no se repitan los q ya pasaron
                                        g2 = g + cost
                                        #h2 = heuristic[x2][y2]
                                        #actual = (x2,y2)
                                        #h2 = heuristic(goal,actual)
                                        #f2 = h2 + g2
                                        open.append([g2, x2, y2])
                                        closed[x2][y2] = 1 
                                        #came_from[(x2,y2)]= (x,y)  #elimina los caminos que no y los sustituye por camino correcto
                                        #delta_ways[(x,y)] = delta_name[i]
    value[0][0]=0
    print("Reverse pathway: ")
    for i in range(len(value)):
        print("%s"%(value[i]))

compute_value3(grid,goal,cost)
input()

def compute_value4(grid,goal,cost):
    #this implementations propaguetes from the goal to the beggining
    #mapeo y puede con mapas grandes y pequeños
    #pero no es eficiente
    value=[[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change=True
    while change:
        change=False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0]==x and goal[1]==y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y]='*'
                        change=True
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2= x + delta[a][0]
                        y2= y+ delta[a][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                            v2=value[x2][y2]+cost
                            if v2 <value[x][y]:
                                change=True
                                value[x][y]=v2
                                policy[x][y] = delta_name[a]
                                
    print("course implementation: ")
    for i in range(len(grid)):
        print("%s"%(value[i]))
    print("map from everywhere: ")
    for i in range(len(grid)):
        print("%s"%(policy[i]))
    return value

compute_value4(grid,goal,cost)
input()