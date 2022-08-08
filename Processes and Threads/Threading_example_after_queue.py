from threading import Thread, Lock, current_thread
from queue import Queue
import time


# reference: https://www.youtube.com/watch?v=HGOBQPFzWKo at 4:28:00

def worker(qin, lock):
    while True:
        value = qin.get()
        # processing
        while lock:
            print(f'in {current_thread().name} got {value}')
            qin.task_done()


# ? for some reason qin.get() and qin.task_done() is not found by the code completion
# ? plus it isn't working correctly

if __name__ == '__main__':
    qin = Queue()
    lock = Lock()
    num_threads = 8

    for i in range(num_threads):
        thread = Thread(target=worker, args=(qin, lock,))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        qin.put(i)

    qin.join()

    print('\nend main')
