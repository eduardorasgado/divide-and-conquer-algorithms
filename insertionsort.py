#InsertionSort
"""
Ordenamiento por inserción

Funcionamiento
1. Recorremos cada elemento de la lista
2. Cada elemento de la lista se ordena si su izquierda tiene un elemento mayor que el actual
3.Si es correcto el paso anterior, se hace el intercambio de valores
4. El elemento se sigue recorriendo hacia la izquierda hasta que tenga un elemento menor que el

"""

import time
import random

print("Insertion Sort")

def generador_listas():
    size = int(input("introduzca el tamaño de su lista, cuantos miembros: "))
    list_1 = random.sample(range(0,size),size)
    print("Lista generada, aleatoriedad presente...")
    print(list_1)
    time.sleep(2)
    return list_1

def insertion_sort(lista):
    print("This is insertion sort...")
    for i in range(1,len(lista)):
        aux = lista[i]
        j = i -1
        while j >=0 and aux < lista[j]:
            lista[j+1],lista[j] = lista[j],aux
            j -= 1
    return lista

print(insertion_sort(generador_listas()))
input()