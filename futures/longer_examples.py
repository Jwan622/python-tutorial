from concurrent import futures
import threading
import time


# def task(n):
#     print('{}: sleeping {}'.format(
#         threading.current_thread().name,
#         n)
#     )
#     time.sleep(n / 10)
#     print('{}: done with {}'.format(
#         threading.current_thread().name,
#         n)
#     )
#     return n / 10
#
# if __name__ == '__main__':
#     ex = futures.ThreadPoolExecutor(max_workers=2)
#     print('main: starting')
#     results = ex.map(task, range(5, 0, -1))
#     print('main: unprocessed results {}'.format(results))
#     print('main: waiting for real results')
#     real_results = list(results)
#     print('main: results: {}'.format(real_results))
#

# single task
# def task(n):
#     print('{}: sleeping {}'.format(
#         threading.current_thread().name,
#         n)
#     )
#     time.sleep(n / 10)
#     print('{}: done with {}'.format(
#         threading.current_thread().name,
#         n)
#     )
#     return n / 10
#
# if __name__ == '__main__':
#     ex = futures.ThreadPoolExecutor(max_workers=2)
#     print('main: starting')
#     f = ex.submit(task, 5)
#     print('main: future: {}'.format(f))
#     print('main: waiting for results')
#     result = f.result()
#     print('main: result: {}'.format(result))
#     print('main: future after result: {}'.format(f))



# futures_future_callback.py
# from concurrent import futures
# import time
#
#
# def task(n):
#     print('{}: sleeping'.format(n))
#     time.sleep(0.5)
#     print('{}: done'.format(n))
#     return n / 10
#
#
# def done(fn):
#     if fn.cancelled():
#         print('{}: canceled'.format(fn.arg))
#     elif fn.done():
#         error = fn.exception()
#         if error:
#             print('{}: error returned: {}'.format(
#                 fn.arg, error))
#         else:
#             result = fn.result()
#             print('{}: value returned: {}'.format(
#                 fn.arg, result))
#
#
# if __name__ == '__main__':
#     ex = futures.ThreadPoolExecutor(max_workers=2)
#     print('main: starting')
#     f = ex.submit(task, 5)
#     f.arg = 5
#     f.add_done_callback(done)
#     result = f.result()



# cancelling. A Future can be canceled, if it has been submitted but not started, by calling its cancel() method. that's why we see we did not cancel 9 and 10 because they were submitted.
# from concurrent import futures
# import time
#
#
# def task(n):
#     print('{}: sleeping'.format(n))
#     time.sleep(0.5)
#     print('{}: done'.format(n))
#     return n / 10
#
#
# def done(fn):
#     if fn.cancelled():
#         print('{}: canceled'.format(fn.arg))
#     elif fn.done():
#         print('{}: not canceled'.format(fn.arg))
#
#
# if __name__ == '__main__':
#     ex = futures.ThreadPoolExecutor(max_workers=2)
#     print('main: starting')
#     tasks = []
#
#     for i in range(10, 0, -1):
#         print('main: submitting {}'.format(i))
#         f = ex.submit(task, i)
#         f.arg = i
#         f.add_done_callback(done)
#         tasks.append((i, f))
#
#     for i, t in reversed(tasks):
#         if not t.cancel():
#             print('main: did not cancel {}'.format(i))
#
#     ex.shutdown()


# exceptions
from concurrent import futures

def task(n):
    print('{}: starting'.format(n))
    raise ValueError('the value {} is no good'.format(n))

if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    f = ex.submit(task, 5)

    error = f.exception()
    print('main: error: {}'.format(error))

    try:
        result = f.result()
        # If result() is called after an unhandled exception is raised within a task function, the same exception is re-raised in the current context.
    except ValueError as e:
        print('main: saw error "{}" when accessing result'.format(e))
