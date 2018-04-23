#Binary search
import random
import time

def binary_search(sequence,value):
    if len(sequence) == 1:
        return sequence[0] == value
    start = 0
    end = len(sequence)-1
    found = False 
    
    if sequence[0] < sequence[1]:
        while start <= end:
            mid = (start+end)//2  #decimal gets trucated
            print(sequence[mid])
            if value==sequence[mid]:
                found = True
                break
            elif value > sequence[mid]:
                start = mid+1               #el caso ascendente
            else:
                end = mid-1
                
    elif sequence[0] > sequence[1]:
        while start <= end:
            mid = (start+end)//2  #decimal gets trucated
            print(sequence[mid])
            if value==sequence[mid]:
                found = True
                break
            elif value > sequence[mid]:
                end = mid-1               #el caso descendente
            else:
                start = mid+1
    return mid,found

def linear_search(sequence,value):
    found = False
    for i in range(len(sequence)):
        #print(sequence[i],end=" ")
        if sequence[i]==value:
            
            found = True
            break
    return sequence[i], found, "en el indice: %d"%(i)
    
input("Binary= press para buscar ascendente: [0,1,2,3,4...]")
first_search = [i for i in range(20000000) if i%2==0]
#print(first_search)
#el algoritmo binary search no funciona para busquedas en listas en descenso
#la lista necesita estar ordenadas
#complejidad: O(log n)
print(binary_search(first_search,14824640))

input("Binary= press para buscar decendente: [200000000,199999999...]")
first_search.reverse()
print(binary_search(first_search,14824640))
time.sleep(1)
print("busqueda lineal...")
new_list = [3,6,15,4,7,5,8,25,4,27,2,1]
print(new_list)
print(linear_search(new_list,25))

input("el caso de un arreglo de un miembro: ")
array = [3]
print(binary_search(array,4))

input()