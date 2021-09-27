from concurrent.futures import ProcessPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(3)
    return message


pool = ProcessPoolExecutor(3)

if __name__ == '__main__':
    future = pool.submit(return_after_5_secs, ("hello"))
    print(future.done())
    sleep(5)
    print(future.done())
    print("Result: " + future.result())

"""
It works perfectly! But of course, we would want to use the ProcessPoolExecutor for CPU intensive tasks. The ThreadPoolExecutor is better suited for network operations or I/O.

While the API is similar, we must remember that the ProcessPoolExecutor uses the multiprocessing module and is not affected by the Global Interpreter Lock. However, we can not use any objects that is not picklable. So we need to carefully choose what we use/return inside the callable passed to process pool executor.
"""
