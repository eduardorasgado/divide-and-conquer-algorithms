#listing
#representacion de grafos
a,b,c,d,e,f,g,h = range(8)

N = [{b:2,c:1,d:3,e:9,f:4},         #a
    {c:4,e:3},                      #b
    {d:8},                          #c
    {e:7},                          #d
    {f:5},                          #e
    {c:2,g:2,h:2},                  #f
    {f:1,h:6},                      #g
    {f:9,g:8}]                      #h

print(b in N[a])  #neighborhood membership/es vecino b de a??
print(len(N[f]))  #degree of f
print(N[a][b])  #edge weight for (a,b)
input()

#matrix for graphs
#matriz de adyacencia

#     a b c d e f g h
M = [[0,1,1,1,1,1,0,0], #a
    [0,0,1,0,1,0,0,0],  #b
    [0,0,0,1,0,0,0,0],  #c
    [0,0,0,0,1,0,0,0],  #d
    [0,0,0,0,0,1,0,0],  #e
    [0,0,0,1,0,0,1,1],  #f
    [0,0,0,0,0,1,0,1],  #g
    [0,0,0,0,0,1,1,0]]  #h

print(sum(M[a]))
input()

#representacionde nodos con infinito a traves de matrices:
#a weight matrix with infinite weighr for missing edges
print("------------------------------")
a,b,c,d,e,f,g,h = range(8)
_ = float('inf')

#     a b c d e f g h
G = [[0,2,1,3,9,4,_,_], #a
    [_,0,4,_,3,_,_,_],  #b
    [_,_,0,8,_,_,_,_],  #c
    [_,_,_,0,7,_,_,_],  #d
    [_,_,_,_,0,5,_,_],  #e
    [_,_,2,_,_,0,2,2],  #f
    [_,_,_,_,_,1,0,6],  #g
    [_,_,_,_,_,9,8,0]]  #h

print(G[a][b] < _)

print(G[c][e] < _)

print(sum(1 for g in G[a] if g < _)-1) #degree
#note: 1 is substracted from G[a] because we dont want the o from the diagonal

input()

