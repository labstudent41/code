from threading import Thread
from time import sleep


def palindrome():
    for num in range(1655, 1665):
        rev, n = 0, num
        while (n != 0):
            rev = rev * 10 + (n % 10)
            n //= 10

        if rev == num:
            print("Palindrome : ", num)
        else:
            print("Not palindrome : ", num)
        sleep(1)


def armstrong():
    for num in range(150, 160):
        total, n = 0, num
        while (n != 0):
            total += (n % 10) ** 3
            n //= 10

        if num == total:
            print("Armstrong : ", num)
        else:
            print("Not an armstrong : ", num)
        sleep(1)


# Main
t1 = Thread(target=palindrome)
t2 = Thread(target=armstrong)

t1.start()
t2.start()

t1.join()
t2.join()
