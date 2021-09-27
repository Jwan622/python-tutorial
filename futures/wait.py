from concurrent.futures import ThreadPoolExecutor, wait, as_completed, FIRST_COMPLETED
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

    done, not_done = wait(futures, return_when=FIRST_COMPLETED)
    print(f"done: {done}")
    print(f"not_done: {not_done}")
    for f in done:
        print(f.result())


"""
We can control the behavior of the wait function by defining when it should return. We can pass one of these values to the return_when param of the function: FIRST_COMPLETED, FIRST_EXCEPTION and ALL_COMPLETED. By default, it’s set to ALL_COMPLETED, so the wait function returns only when all futures complete. But using that parameter, we can choose to return when the first future completes or first exception encounters.
"""
