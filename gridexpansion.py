#Grid expansionA*
#Mapping the path
grid1 = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

grid = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
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

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2)+abs(y1-y2)

def search(grid,init,goal,cost):

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand =[[-1]*len(grid[0])for i in grid]
    x = init[0]
    y = init[1]
    g = 0
    #h = heuristic[x][y]
    h = heuristic(goal,init)
    f = g + h
    #priority Queue
    open = [[f, h, g, x, y]]
    #expand[x][y] = g
    count =0
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
            x = next[3]
            y = next[4]
            g = next[2]
            path_way[(next[3],next[4])] = next[2]
            expand[x][y] = count
            count +=1   
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                
                for i in range(len(delta)): #este es el ciclo para aplicar el filtro de los movimientos
                    x2 = x + delta[i][0]   #actual x mas el movimiento delta(x)
                    y2 = y + delta[i][1]   #actual y mas el movimiento en delta(y)
                    
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]): #filtro de delimitacion de "terreno"
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0: #verificar q no se repitan los q ya pasaron
                            g2 = g + cost
                            #h2 = heuristic[x2][y2]
                            actual = (x2,y2)
                            h2 = heuristic(goal,actual)
                            f2 = h2 + g2
                            open.append([f2, h2, g2, x2, y2])
                            closed[x2][y2] = 1 
                            came_from[(x2,y2)]= (x,y)  #elimina los caminos que no y los sustituye por camino correcto
                            delta_ways[(x,y)] = delta_name[i]
    
    start = (init[0],init[1])
    current = (goal[0],goal[1])
    path = [current]   #regresa el camino mas corto
    while current != start:
        current = came_from[current]
        path.append(current)       
    path.reverse()
    #seteando el camino mas corto pero con las señales
    path_signals = {}
    for way in range(len(path)):
        for key in delta_ways:
            if key == path[way]:
                path_signals[key] = delta_ways[key]
    draw = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    for way in range(len(path)):
        for i in range(len(draw)):
            for j in range(len(draw[i])):
                verify = (i == path[way][0])
                verify2 = (j == path[way][1])
                if verify and verify2:
                    if i == goal[0] and j==goal[1]:
                        draw[i][j]= '*'
                    else:
                        draw[i][j]= path_signals[(i,j)]
                    
                
    print("path_signals: ")            
    print(path_signals)
    print("came_from: ")
    print(came_from)
    #print("delta_ways ")
    #print(delta_ways)
    print("costs:")
    print(path_way)
    print("expand map")
    for i in range(len(expand)):
        print("%s\n"%(expand[i]))
    print("signal map:")
    for i in range(len(draw)):
        print("%s\n"%(draw[i]))
    print("final cost in steps:")
    print(len(path)-1)
    print("from came_from we get the shortest path: ")
    return path
    #return next
    #return expand
try:
    print(search(grid,init,goal,cost))
except Exception as e:
    print("fail, no path possible")
    print(str(e))

input()

