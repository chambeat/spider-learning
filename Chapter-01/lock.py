""" 互斥锁 """
# import threading
from threading import Thread, Lock
import time

count = 0  # initialize variable 'count'


# class MyThread(threading.Thread):
class MyThread(Thread):
    def __init__(self):
        # threading.Thread.__init__(self)
        super().__init__()

    def run(self):
        global count  # call and globalize variable 'count'
        lock.acquire()  # 2. lock up
        temp = count + 1
        time.sleep(0.001)  # remove this line with no LOCK, then 'count' would be 1000
        count = temp
        lock.release()  # 3. unlock


lock = Lock()  # 1. initialize a Lock object
threads = []
for _ in range(1000):
    thread = MyThread()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(f'Final count is: {count}')
