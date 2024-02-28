from threading import Thread
from time import sleep

def rev():
    for n in range(20, 25):
        num = n
        reverse = 0
        while n:
            reverse = reverse * 10 + (n % 10)
            n //= 10
        print("Reverse of %d is %d " % (num, reverse))
        sleep(0.2)

def square():
    for i in range(35, 40):
        print("Square of %d is %d " % (i, i*i))
        sleep(0.2)

# Main
t1 = Thread(target=rev)
t2 = Thread(target=square)

t1.start()
t2.start()
# t1.join()
# t2.join()
