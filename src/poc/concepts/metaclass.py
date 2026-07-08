class TestMetaClass(type):
    """
    This will be called before class creation
    """
    def __new__(cls, cls_name, bases, cls_dict):
        print(f"__new__ method called with cls = {cls.__name__}, cls_name = {cls_name}, "
              f"bases = {bases}, cls_dict = {cls_dict}")
        return super().__new__(cls, cls_name, bases, cls_dict)

    def __call__(cls, *args, **kwargs):
        """
        This will be called before __init__ call of the class, i.e. before object creation
        """
        print(f"__call__ method called with cls = {cls.__name__}, args = {args}, kwargs = {kwargs}")
        return super(TestMetaClass, cls).__call__(*args, **kwargs)


class TestClass(metaclass=TestMetaClass):
    def __init__(self, value: int):
        self.value = value
        print(f"__init__ method called with {self}, {value}")


class TestSubClass(TestClass):
    pass


if __name__ == '__main__':
    print("------------")
    t = TestClass(1)
    print(f"Type of t = {type(t).__name__}, value = {t.value}")

    print("------------")
    ts = TestSubClass(1)
    print(f"Type of ts = {type(ts).__name__}, value = {ts.value}")
