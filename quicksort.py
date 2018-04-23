#Quicksort
#divide and conquert algorithm witch is recursive too
import random

def quick_sort(list_sort,low_index,high_index):
    if high_index - low_index > 0:
        p = partition(list_sort,low_index,high_index)
        quick_sort(list_sort,low_index,p-1)
        quick_sort(list_sort,p+1,high_index)
        
        
def partition(list_sort,low_index,high_index):
    divider = low_index
    pivot = high_index
    for i in range(low_index,high_index):
        if list_sort[i] < list_sort[pivot]:
            list_sort[i],list_sort[divider] = list_sort[divider],list_sort[i]
            divider += 1
    list_sort[pivot],list_sort[divider] = list_sort[divider],list_sort[pivot]
    return divider

def starting():
    length =int(input("inserte la longitud de su lista es decir cuantos miembros: "))
    testlist = random.sample(range(0,length),length)
    #print("la lista es la siguiente: ",testlist)
    input("la lista está preparada, presione y espere...")
    quick_sort(testlist,0,length-1)
    pressing = str(input("Lista ordenada, desea verla?"))
    if pressing == "si" or pressing == "Si" or pressing == "SI":
        print(testlist)
    elif pressing == "no" or pressing == "NO" or pressing == "No":
        pass
    else:
        print("Bye")
        

starting()
input()