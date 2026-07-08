
class SingletonCLS(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonCLS, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class SingletonClass1(metaclass=SingletonCLS):
    def __init__(self, value: int):
        self.value = value
        print("New object created")


class SingletonCLSandArgs(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        key = (cls, args, str(kwargs))
        if key not in cls.__instances:
            cls.__instances[key] = super(SingletonCLSandArgs, cls).__call__(*args, **kwargs)
        return cls.__instances[key]


class SingletonClass2(metaclass=SingletonCLSandArgs):
    def __init__(self, value: int):
        self.value = value
        print(f"New object created with value = {value}")


if __name__ == '__main__':
    a = SingletonClass1(1)
    b = SingletonClass1(2)
    assert a is b
    assert a.value is b.value
    print("Both SingletonClass1 are same object")

    c = SingletonClass2(3)
    d = SingletonClass2(4)
    e = SingletonClass2(4)
    assert c is not d
    assert c.value != d.value
    print("Both SingletonClass2 with different value are not same object")
    assert d is e
    print("Both SingletonClass2 with same value are same object")
