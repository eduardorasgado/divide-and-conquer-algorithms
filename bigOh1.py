#Little algorithm to find a dupplicate entries in an array

A = [7,5,8,2,4,3,7,9,6,0,4]

def duplicate_entries(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                yield A[i]

for i in duplicate_entries(A):
    print(i)
    
input()