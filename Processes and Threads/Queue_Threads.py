from threading import Thread, Lock
from queue import Queue
import time

if __name__ == '__main__':
    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3, 2, 1

    first = q.get()
    print(first)

    q.task_done()
    q.join
    # block until all items in the queue have been got and processed.
    # tells program that we are done processing with the first queue object.

    print(q.empty())
    # if queue is empty returns true

    print('end main')
