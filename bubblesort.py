#Ordenamiento burbuja

"""
Revisa cada elemento de la lsita con el siguiente elemento. Intercambiándolos de posicion si estan en el orden equivocado

Ejemplo:

4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8
"""
import time
import random

print("Bubble Sort")

def generador_listas():
    size = int(input("introduzca el tamaño de su lista, cuantos miembros: "))
    list_1 = random.sample(range(0,size),size)
    print("Lista generada, aleatoriedad presente...")
    return list_1

def bubble(lista):
    print("lista inicial: ",lista)
    time.sleep(2)
    for i in range(len(lista)):
        #para cada miembro de la lista
        for x in range(len(lista)-1):
            print("Bubbles!...")
            #comparamos todos los miembros entre parejas, 0-1, 1-2,2-3.3-4...etc
            if lista[x] >lista[x+1]:
                lista[x], lista[x+1] = lista[x+1],lista[x]
                print(lista)
                time.sleep(0.1)
            else:
                pass
    return "Lista final: {}".format(lista)
    

print(bubble(generador_listas()))
input()
            