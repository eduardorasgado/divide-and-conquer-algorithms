#Listas,coleccion de datos
lista =  [1,22,33,45,5,6]

cad = []
for x in range(len(lista)):
    cad.append(x)
    
get = dict(zip(cad,lista))
print(get)

print("-"*20)
for x in lista:
    print(x)
    
print("______________:)__________")
for i in range(len(lista)):
    print("index[%d] => %d"%(i,lista[i]))
    
lista += [15]
print(lista)
print(lista[:-3])
print(lista[-3:])



