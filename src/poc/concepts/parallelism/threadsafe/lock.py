import threading
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Pool


class Lock:
    def __init__(self, value: int):
        self.value = value
        self.__lock = threading.Lock()
        print(f"Initial value is {self.value}")

    def thread_unsafe_method(self, i: int):
        self.value += 1
        print(f"{i}. After adding 1, value is {self.value}")

    def threadsafe_method(self, i: int):
        with self.__lock:
            self.thread_unsafe_method(i)


if __name__ == '__main__':
    ob = Lock(value=0)
    indices = [i for i in range(1, 20)]
    with ThreadPoolExecutor(2) as tp:
        tp.map(ob.threadsafe_method, indices)
    with Pool(2) as tp:
        tp.map(ob.threadsafe_method, indices)

    print("--------------------------------")

