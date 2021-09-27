from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from time import sleep
from random import randint


def return_after_5_secs(num):
    sleep(randint(1, 5))
    return "Return of {}".format(num)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    futures = []
    for x in range(5):
        futures.append(pool.submit(return_after_5_secs, x))

    for x in as_completed(futures):
        print(x.result())

# the numbers return in different order as completed... it returns whatever completes frist.
# The as_completed() function takes an iterable of Future objects and starts yielding values as soon as the futures start resolving. The main difference between the aforementioned map method with as_completed is that map returns the results in the order in which we pass the iterables. That is the first result from the map method is the result for the first item. On the other hand, the first result from the as_completed function is from whichever future completed first.
