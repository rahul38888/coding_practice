
class MyClass:
    def __init__(self, lookup: set):
        self.lookup = lookup

    def __contains__(self, item):
        return item in self.lookup

    def __len__(self):
        return len(self.lookup)

    def __repr__(self):
        return f"MyClass({self.lookup})"

    def __str__(self):
        return repr(self)


if __name__ == '__main__':
    obj = MyClass({1, 3, 5, 7, 2, 4, 6, 8})
    print(obj)
    print(f"4 in: {4 in obj}")
    print(f"10 in: {10 in obj}\nLength: {len(obj)}")
    print(f"Length: {len(obj)}")
    print(obj)
