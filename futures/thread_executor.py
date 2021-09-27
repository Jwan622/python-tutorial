from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(3)
    return message


pool = ThreadPoolExecutor(3)


if __name__ == '__main__':
    future = pool.submit(return_after_5_secs, ("hello"))
    print(f"what is future: {future}")
    print(f"should not be done yet: {future.done()}")
    sleep(5)
    print(f"should be done here: {future.done()}")
    print(future.result())

"""
We first construct a ThreadPoolExecutor with the number of threads we want in the pool. By default the number is 5 but 
we chose to use 3 just because we can ;-). Then we submitted a task to the thread pool executor which waits 5 seconds 
before returning the message it gets as it’s first argument. When we submit() a task, we get back a Future. As we can 
see in the docs, the Future object has a method – done() which tells us if the future has resolved, that is a value 
has been set for that particular future object. When a task finishes (returns a value or is interrupted by an 
exception), the thread pool executor sets the value to the future object.
"""
