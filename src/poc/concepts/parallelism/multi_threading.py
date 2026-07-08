import os
import time
from threading import Thread


def cpu_bound_counter(n: int):
    while n > 0:
        n -= 1


def io_bound_read_file(file_name: str):
    with open(file_name, "r") as f:
        f.readlines()


if __name__ == '__main__':
    N = 1000000
    start = time.time()
    cpu_bound_counter(N)
    print(f"Single threaded CPU bound, time = {time.time() - start}")

    t1 = Thread(target=cpu_bound_counter, args=(N//2, ))
    t2 = Thread(target=cpu_bound_counter, args=(N//2, ))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Multi threaded CPU bound, threads = 2, time = {time.time() - start}")

    files = ["test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt",
             "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt",
             "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt"]
    path = os.path.dirname(os.path.realpath(__file__))

    start = time.time()
    for f in files:
        io_bound_read_file(f"{path}\\{f}")
    print(f"Single threaded I/O bound, time = {time.time() - start}")

    ts = [Thread(target=io_bound_read_file, args=(f"{path}\\{f}", )) for f in files]
    start = time.time()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print(f"Multi threaded I/O bound, threads = {len(files)}, time = {time.time() - start}")

