import time
from multiprocessing import Process, Value, Lock


# def func(val, lock):
#     for i in range(50):
#         time.sleep(0.01)
#         with lock:
#             val.value += 1
#
# if __name__ == '__main__':
#     v = Value('i', 0)
#     lock = Lock()
#     procs = [Process(target=func, args=(v, lock)) for i in range(10)]
#
#     for p in procs: p.start()
#     for p in procs: p.join()
#
#     print(v.value)


## A value and a lock may appear like too much baggage to carry around at all times. So, we can create a simple
# "synchronized shared counter" object to encapsulate this functionality:

class Counter(object):
    def __init__(self, initval=0):
        self.val = Value('i', initval)
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.val.value += 1

    def value(self):
        with self.lock:
            return self.val.value


def func(counter):
    for i in range(50):
        time.sleep(0.01)
        counter.increment()


if __name__ == '__main__':
    counter = Counter(0)
    procs = [Process(target=func, args=(counter,)) for i in range(10)]

    for p in procs: p.start()
    for p in procs: p.join()

    print(counter.value())
