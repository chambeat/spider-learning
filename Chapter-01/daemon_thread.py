""" 守护线程 """
import threading
import time


def target(second):
    print(f'Threading {threading.current_thread().name} is running.')
    print(f'Threading {threading.current_thread().name} sleep {second}s.')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} ended.')


print(f'Threading {threading.current_thread().name} is running.')
t1 = threading.Thread(target=target, args=[1])
t1.start()
t2 = threading.Thread(target=target, args=[8])
t2.setDaemon(True)
t2.start()
print(f'Threading {threading.current_thread().name} ended.')
