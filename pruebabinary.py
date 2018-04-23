#coparamos los tiempos de procesado entre los dos tipos de implementaciones basicas
#binary search es mejor al observarse.
import random
import timeit

print("El procesado de encontrar numeros con binary search en un rango de 20000000 es: ")
print(timeit.timeit("""
def binary_search(sequence,value):
    start = 0
    end = len(sequence)-1
    found = False 
    while start <= end:
        mid = (start+end)//2  #decimal gets trucated
        print(sequence[mid])
        if value==sequence[mid]:
            found = True
            break
        elif value > sequence[mid]:
            start = mid+1
        else:
            end = mid-1
    return mid,found
first_search = [i for i in range(20000000) if i%2==0]
#print(first_search)
#el algoritmo binary search no funciona para busquedas en listas en descenso
#la lista necesita estar ordenadas
#complejidad: O(log n)
binary_search(first_search,14824640)""",number=1))
input()

print("El procesado de encontrar numeros con linear search en un rango de 20000000 es: ")
print(timeit.timeit("""first_search = [i for i in range(20000000) if i%2==0]
def linear_search(sequence,value):
    found = False
    for i in range(len(sequence)):
        #print(sequence[i],end=" ")
        if sequence[i]==value:
    
            found = True
            break
    return sequence[i], found
n, k = linear_search(first_search,14824640)
print(n,k)""",number=1))

input()