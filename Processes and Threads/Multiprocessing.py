# Reference = https://www.youtube.com/watch?v=HGOBQPFzWKo&t=7245s at 4:00:00 #? having an issue with the code

from multiprocessing import Process
import os
import time


def square_nums():
    for i in range(10):
        i * i
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()
# os.cpu_count() might be counting the threads #? suppose to count the cpu's
# print(num_processes)

# create processes
for i in range(num_processes):
    p = Process(target=square_nums)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print('end main')

# Process takes 2 arguments. Target which is a callable object or function that is then executed by this program Process
# args = (xxxx, yyyy) is the second argument.
