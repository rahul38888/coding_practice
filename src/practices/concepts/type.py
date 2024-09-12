

def my_func(self, i: int) -> int:
    return i * self.__m


class Math:
    def __init__(self, n: int):
        self.__n = n

    def n_times(self, i: int) -> int:
        return self.__n * i


if __name__ == '__main__':
    print(type(Math))
    # <class 'type'>
    math = Math(6)
    print(type(math))
    # <class '__main__.TestClass'>

    print(math.n_times(2))
    # 12

    print("-----------")

    MyMath = type("MyMath", (Math, ), dict(__m=4, m_times=my_func))
    myMath = MyMath(6)
    print(type(MyMath))
    # <class 'type'>
    print(type(myMath))
    # <class '__main__.MyMath'>
    print(myMath.n_times(2))
    # 12
    print(myMath.m_times(2))
    # 8

