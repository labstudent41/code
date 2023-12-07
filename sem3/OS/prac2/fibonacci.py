from threading import Thread
from time import sleep


def fibonacci():
    n = 30
    fterm, sterm, nterm = 0, 1, 1
    while nterm <= n:
        print("Fibonacci : ", nterm)
        sleep(0.3)
        fterm = sterm
        sterm = nterm
        nterm = fterm + sterm


def num():
    for i in range(11):
        print("Number : ", i)
        sleep(0.2)


# Main
print("Multithreading")
t1 = Thread(name="Numbers", target=num)
t2 = Thread(name="Fibonacci", target=fibonacci)
t1.start()
t2.start()
t1.join()
t2.join()
