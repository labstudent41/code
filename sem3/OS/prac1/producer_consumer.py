from threading import Thread, Condition
import time
import random

queue = []
max_num = 10
condition = Condition()


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == max_num:
                print("Queue is full, producer is waiting...")
                condition.wait()
                print("Space in queue, consumer notified producer")
                break
            num = random.choice(nums)
            queue.append(num)
            print("Produced : ", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer is waiting...")
                condition.wait()
                print("Producer added something, notified consumer.")
            num = queue.pop()
            print("Consumed : ", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


t1 = ProducerThread()
t2 = ConsumerThread()

t1.start()
t2.start()

t1.join()
t2.join()
