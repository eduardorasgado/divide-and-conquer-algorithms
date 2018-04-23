#Merge sort
import random

def arrays():
    
    give_me = int(input("Se hara un arreglo con el numero de numeros que nos proporcione, trate que sea una gran cantidad: "))
    try:
        int(give_me)
        match = [i for i in range(give_me)]
        #print(match)
        random.shuffle(match)
        print("Los numeros se han mezclado aleatoriamente")
        #print(match)
        input("press enter and await for merge sort...")
    except:
        print("again please:")
        arrays()
    return match
    
def merge_sort(match):
    n = int(len(match)/2)
    output_array = []
    if len(match) < 2:
        return match
    #recursividad
    first_array = merge_sort(match[:n])
    second_array = merge_sort(match[n:])
    i = 0
    j = 0
    
    while i < len(first_array) and j < len(second_array):
        if first_array[i] > second_array[j]:
            output_array.append(second_array[j])
            j += 1
        elif second_array[j] > first_array[i]:
            output_array.append(first_array[i])
            i += 1
                
    output_array +=first_array[i:]
    output_array += second_array[j:]
    #print("...")
    return output_array
    
    
finished = merge_sort(arrays())
if finished:
    print("listo")
    print(finished)
input()
    
#complejidad: O(nlogn)
#o tambien 6nlog2n + 6n