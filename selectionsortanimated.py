import pylab
import random

def selectionsort_anim(a):
    x = range(len(a))
    for j in range(len(a)-1):
        iMin = j
        for i in range(j+1,len(a)):
            if a[i] < a[iMin]: #find the smallest value
                iMin = i
            if iMin != j: #place the value into its proper location
                a[iMin],a[j]= a[j],a[iMin]
        #plotting
        pylab.plot(x,a,'k.',markersize=6)
        pylab.savefig("selectionsort/img"+"%04d"%(j)+".png")
        pylab.clf()#figure clear
#running the algorithm
a = [i for i in range(300)]#initializing the array
random.shuffle(a)
selectionsort_anim(a)