import time
from functools import wraps


class AllDone:
    def __init__(self, func):
        """
        Decorator defined by a class
        """
        self.__func = func

    def __call__(self, *args, **kwargs):
        print(f"AllDone: Starting executing `{self.__func.__name__}`")
        val = self.__func(*args, **kwargs)
        print(f"AllDone: Done executing `{self.__func.__name__}`")
        return val


def declaimer(func):
    """
    Decorator defined by a function
    """
    def declair(*args, **kwargs):
        print(f"Declair: `{func.__name__}` called with args = {args} and kwargs = {kwargs}")
        val = func(*args, **kwargs)
        print(f"Declair: `{func.__name__}` finished")
        return val

    return declair


def timeme(func):
    """
    Decorator defined by a function
    """
    def timer(*args, **kwargs):
        print(f"Timer: `{func.__name__}` called with args = {args} and kwargs = {kwargs}")
        start = time.time()
        val = func(*args, **kwargs)
        print(f"Timer: Time taken to execute `{func.__name__}` = {time.time() - start}")
        return val

    return timer


@AllDone
@declaimer
@timeme
def add(*values):
    print(f"Add: add called with args = {values}")
    s = 0
    for v in values:
        s += v
    return s


if __name__ == '__main__':
    print(add(1, 2, 3, 4, 5))
