#SelectionSort

"""
Ordenamiento por seleccion
Es un algoritmo que consiste en ordenar de manera ascendente o descendente

Funcionamiento:
-Buscar el dato mas pequeño de la lista
-Intercambiarlo por el actual
-Seguir buscando el dato mas pequeño de la lista
-Intercambiarlo por el actual
-Repeticion sucesiva

"""

import time
import random

print("Selection Sort")

def generador_listas():
    size = int(input("introduzca el tamaño de su lista, cuantos miembros: "))
    list_1 = random.sample(range(0,size),size)
    print("Lista generada, aleatoriedad presente...")
    print(list_1)
    return list_1

def selection_sort(lista):
    time.sleep(2)
    print("empezamos...")
    for i in range(len(lista)):
        for x in range(i+1,len(lista)):
            if lista[x] < lista[i]:
                lista[x], lista[i] = lista[i],lista[x]
                
    return lista

print(selection_sort(generador_listas()))
input()
        
    