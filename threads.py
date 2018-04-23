#thread
import threading
import time
#taking advantage og threading.currentThread().getName() function to debug the state of your threads
def worker():
    print(threading.currentThread().getName(),"Starting")
    time.sleep(2)
    print(threading.currentThread().getName(),"Exiting")


w = threading.Thread(name="worker",target=worker) #given a name to the thread
w2 = threading.Thread(target=worker) #use default name

w.start()
w2.start()
    

#debug messages can be printed to log messages as well in logging module
input()