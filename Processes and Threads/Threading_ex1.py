# Reference = https://www.youtube.com/watch?v=HGOBQPFzWKo&t=7245s at 4:00:00 #? having an issue with the code

from threading import Thread
import os
import time


def square_nums():
    for i in range(10):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_nums)
        threads.append(thread)

    # start
    for thread in threads:
        thread.start()

    # join
    for thread in threads:
        thread.join()

    print('end main')

# Process takes 2 arguments. Target which is a callable object or function that is then executed by this program Process
# args = (xxxx, yyyy) is the second argument.
