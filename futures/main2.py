import time
import requests
from concurrent.futures import ThreadPoolExecutor

url_list = ['https://docs.python.org/3/library/concurrent.futures.html', \
            'https://technokeeda.com',
            'https://google.com',
            'https://airbnb.com']


def get_sequential_get(urls):
    """
    Function which does a get requests
    one after the other
    """
    result = []
    for url in urls:
        response = requests.get(url)
        result.append([response, response.status_code])
    return result


def get_futures_get(urls):
    results = []
    currs = ThreadPoolExecutor(max_workers=5)
    # This initializes a pool of threads which can at any point contain a maximum of 5 threads. Whenever a tasks is submitted to a thread pool executor it spins up a new thread if no other thread is idle and the number of busy threads is less than the max_workers flag defined.
    for url in urls:
        currs.submit(worker_func, url, results)
        # Here we iterate over the list of all the urls and submit each url to be processed by a worker function that we have already written. Notice how we pass the function reference and the params separately.
    currs.shutdown(wait=True)
    #This line tells the thread pool to shutdown. You will not be able to submit anymore tasks to this thread pool.
    return results


def worker_func(url, result_list):
    print(f"IN WORKER FUNCTION: {url}")
    response = requests.get(url)
    result_list.append([response, response.status_code])


def calculate_function_time(curr_func, **kwargs):
    start = time.localtime()
    curr_func(**kwargs)
    end = time.localtime()
    return end.tm_sec - start.tm_sec


if __name__ == '__main__':
    print('Time taken by normal implementation {} seconds'.format(
        calculate_function_time(get_sequential_get, **{'urls': url_list}))
    )
    print('Time taken by futures implementation {} seconds'.format(
        calculate_function_time(get_futures_get, **{'urls': url_list}))
    )

