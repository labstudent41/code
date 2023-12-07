from threading import Thread, Lock
from time import sleep
from random import random

lock = Lock()
x = [1]


def reader(lock, data):
    lock.acquire()
    print("\nReading...")
    print("Value = %s" % data)
    sleep(random())
    lock.release()


def writer(lock, data):
    lock.acquire()
    print("\nWriting...")
    data.append(data[-1] + 1)
    sleep(random())
    lock.release()


for i in range(5):
    if random() > 0.5:
        Thread(target=reader, args=(lock, x)).start()
    else:
        Thread(target=writer, args=(lock, x)).start()
