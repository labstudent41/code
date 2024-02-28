import threading
from time import sleep

def upper(x):
    print("Upper : %3d : %s" % (x, chr(x)))

def lower(x):
    print("Lower : %3d : %s" % (x, chr(x)))

def print_thread(x):
    if x <= 90:
        upper(x)
    else:
        lower(x)
    sleep(0.2)


thread_list = []
thread_upper = []
thread_lower = []

for i in range(65, 123):
    t = threading.Thread(target=print_thread, args=(i,))
    if i <= 90:
        thread_upper.append(t)
    else:
        thread_lower.append(t)

thread_list.extend(thread_upper)
thread_list.extend(thread_lower)

for thread in thread_list:
    thread.start()
    thread.join()

# print(thread_upper)
# print(thread_lower)
