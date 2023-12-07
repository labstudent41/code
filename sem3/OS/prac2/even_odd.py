import threading
from time import sleep
def print_thread(x):
    if x % 2 == 0:
        even(x)
    else:
        odd(x)
    sleep(0.2)

def even(x):
    print("even : %2d" % x)
def odd(x):
    print("odd  : %2d" % x)

thread_list = []

for i in range(1, 20):
    t = threading.Thread(target=print_thread, args=(i,))
    thread_list.append(t)

for thread in thread_list:
    thread.start()
    thread.join()
