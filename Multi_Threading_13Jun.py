#-------- Sequential Execution -------
# Code will run one by one 

##import time
##
##def fun():
##    print("one")
##    print(time.ctime())
##    time.sleep(4)
##
##def fun2():
##    print("two")
##    print(time.ctime())
##
##
##fun()
##fun2()
          

# ---- Multi Threading ----

##Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

import time
import threading

def fun():
    print("one")
    print(time.ctime())
    

def fun2():
    print("Two")
    print(time.ctime())


t1 =threading.Thread(target = fun)
t2 = threading.Thread(target = fun2)

t1.start()
t2.start()


##import time
##import threading
##
##def fun(name,delay):
##    counter = 0
##    while counter <5:
##        counter+=1
##        print(name)
##        print(time.ctime())
##        time.sleep(delay)
##    
##
##t1 =threading.Thread(target = fun,args=["Dhoni",2])
##t2 = threading.Thread(target = fun,args=["Kohli",4])
##
##t1.start()
##t2.start()
##
##t1.join()
##t2.join()


##import threading
##  
##def print_cube(num):
##    """
##    function to print cube of given num
##    """
##    print("Cube: {}".format(num * num * num))
##  
##def print_square(num):
##    """
##    function to print square of given num
##    """
##    print("Square: {}".format(num * num))
##  
##if __name__ == "__main__":
##    # creating thread
##    t1 = threading.Thread(target=print_square, args=(10,))
##    t2 = threading.Thread(target=print_cube, args=(10,))
##  
##    # starting thread 1
##    t1.start()
##    # starting thread 2
##    t2.start()
##  
##    # wait until thread 1 is completely executed
##    t1.join()
##    # wait until thread 2 is completely executed
##    t2.join()
##  
##    # both threads completely executed
##    print("Done!")





# Python program to illustrate the concept
# of threading
##import threading
##import os
##  
##def task1():
##    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
##    print("ID of process running task 1: {}".format(os.getpid()))
##  
##def task2():
##    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
##    print("ID of process running task 2: {}".format(os.getpid()))
##  
##if __name__ == "__main__":
##  
##    # print ID of current process
##    print("ID of process running main program: {}".format(os.getpid()))
##  
##    # print name of main thread
##    print("Main thread name: {}".format(threading.current_thread().name))
##  
##    # creating threads
##    t1 = threading.Thread(target=task1, name='t1')
##    t2 = threading.Thread(target=task2, name='t2')  
##  
##    # starting threads
##    t1.start()
##    t2.start()
##  
##    # wait until all threads finish
##    t1.join()
##    t2.join()
