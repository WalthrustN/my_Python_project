from multiprocessing import Pool
import time


def cube(number):
    return number * number * number


if __name__ == '__main__':
    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers)  #
    # ? pool.apply(cube, numbers[1])
    # apply can only be used for one job

    # map will automatically allocate the maximum number of processors available and create different processes, and
    # split the iterable into equal sized chunks and submit to to the function. Now the function will be executed in
    # parallel by different processors.

    pool.close()  #
    # have to close the pool to start it
    pool.join()  #
    # pool.join waits for the pool to process all calculations and return results

    print(result)
