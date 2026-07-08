
class MyClass:
    def __init__(self, collection: list):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        val = self.collection[self.index]
        self.index += 1
        return val

    def __len__(self):
        return len(self.collection)

    def __repr__(self):
        return f"MyClass({self.collection})"

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    obj = MyClass([1, 3, 5, 7, 2, 4, 6, 8])
    print(obj)
    print(f"Length: {len(obj)}")
    for v in obj:
        print(v, end=" ")
    print()

    print(obj)
