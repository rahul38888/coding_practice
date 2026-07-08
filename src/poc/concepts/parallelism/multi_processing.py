import os
import time
from multiprocessing import Pool, Process


def cpu_bound_counter(n: int):
    while n > 0:
        n -= 1


def io_bound_read_file(file_name: str):
    with open(file_name, "r") as file:
        file.readlines()


if __name__ == '__main__':
    N = 1000000
    start = time.time()
    cpu_bound_counter(N)
    print(f"Single process CPU bound, time = {time.time() - start}")

    start = time.time()
    p1 = Process(target=cpu_bound_counter, args=(N//2, ))
    p2 = Process(target=cpu_bound_counter, args=(N//2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Multi processes CPU bound, processes = 2, time = {time.time() - start}")

    files = ["test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt",
             "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt",
             "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt", "test.txt"]
    path = os.path.dirname(os.path.realpath(__file__))

    start = time.time()
    for f in files:
        io_bound_read_file(f"{path}\\{f}")
    print(f"Single process I/O bound, time = {time.time() - start}")

    start = time.time()

    ps = [Process(target=io_bound_read_file, args=(f"{path}\\{f}", )) for f in files]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print(f"Multi processes I/O bound, processes = 4, time = {time.time() - start}")
