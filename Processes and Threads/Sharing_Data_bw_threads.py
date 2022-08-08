# Reference = https://www.youtube.com/watch?v=HGOBQPFzWKo&t=7245s at 4:10:00 #? having an issue with the code

from threading import Thread, Lock
import os
import time

database_value = 0


def increase(lock):
    global database_value

    lock.acquire()
    local_copy = database_value
    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()

    # In the programming world, a global variable in Python means having a scope throughout the program, i.e., a global
    # variable value is accessible throughout the program unless shadowed. A global variable in Python is often declared
    # as the top of the program.

    # because of the thread being locked, it will not switch to thread2 while time.sleep(0.1) so its completes thread1
    # first, then releases the lock so thread2 can be completed. This is to take care of the race condition error that
    # will occur.

    # another way of using lock, using lock as a context manager. This is the preferred method. The context manager
    # acquires and release the lock.

    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == '__main__':
    lock = Lock()
    print('start value', database_value)

    # create threads
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    # remember the target and args have to be written like this

    # start
    thread1.start()
    thread2.start()

    # join
    thread1.join()
    thread2.join()

    print('end value', database_value)

# Process takes 2 arguments. Target which is a callable object or function that is then executed by this program Process
# args = (xxxx, yyyy) is the second argument.
