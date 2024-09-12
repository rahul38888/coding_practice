from collections import deque
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Pool

queue = deque()

if __name__ == '__main__':
    indices = [i for i in range(1, 20)]
    with ThreadPoolExecutor(2) as tp:
        tp.map(lambda i: queue.append(i), indices)
    # with Pool(2) as tp:
    #     tp.map(ob.threadsafe_method, indices)
