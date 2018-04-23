#lento pero seguro, cremiento linear del running time
count = 10**5
nums = []
for i in range(count):
    nums.append(i)
nums.reverse()

print(nums)
input("that was reverse slow...")

#algo para meterlos en reversa desde que aparecen:... ojo, notamos que tarda mucho mas
#crecimiento cuadratico del running time

nums2 = []
for i in range(count):
    nums2.insert(0,i)
    
print(nums2)
input("now...")
"""
#_______________________nesting running time
seq = range(1000)
s = 0
for x in seq:#running time entonces es: n(n+n**2)=n**2+n**3= theta n**3
    for y in seq:  #running time: n
        s+= x*y
    for z in seq:  #running time: n**2
        for w in seq:
            s += x-w
            print(s)
            
print("finally:", s)
#esto es entonces un loop con un running time de theta n**3
input()
"""
seq1 = [[0,1],[2],[3,4,5]]
s = 0
for seq2 in seq1:
    for x in seq2:
        s += x
        print(x,seq2)
        print(s)
print("finally:",s)
input("-----------")
#este es un multiplicador dd numeros de una lista, no se repiten multiplicaciones y no se multiplican uno por el mismo
seq = [0,1,2,3,4,5,6,7,8,9,10]
s = 0
n = len(seq)
for i in range(n-1):
    for j in range(i+1, n):
        s += seq[i] * seq[j]
print(s)       
input()


