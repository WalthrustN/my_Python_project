# Each Process is made up of a bunch of different threads. Threads are essentially different tasks that are running.
# Threads are just a bunch of task that make up a process. They can not be run in parallel, They are run sequentially.
# We can switch between threads to be efficient.
# With the threading module you can set tasks to run after a certain time interval.

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadId, name, count):  # threads that we are creating will countdown from count
        threading.Thread.__init__(self)  # low level stuff going on when we made a new thread.
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting" + self.name + "\n")
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print("Exiting" + self.name + "\n")


class myThread2(threading.Thread):
    def __init__(self, threadId, name, count):  # threads that we are creating will countdown from count
        threading.Thread.__init__(self)  # low level stuff going on when we made a new thread.
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting" + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print("Exiting" + self.name + "\n")


def print_time(name, delay, count):
    while count:  # means while any number except 0:
        time.sleep(4 * delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


threadLock = threading.Lock()

Thread1 = myThread(1, ' Payment', 5)
Thread2 = myThread2(2, ' Sending Email', 10)
Thread3 = myThread2(2, ' Loading Page', 5)

Thread1.start()
Thread2.start()
Thread3.start()
Thread1.join()
Thread2.join()
Thread3.join()
