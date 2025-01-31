
class MyClass:
    def __init__(self, collection: list):
        self.collection = collection

    def reverse_generator(self):
        """
        Generators are a simple and powerful tool for creating iterators.
        They are written like regular functions but use the yield statement
            whenever they want to return data.

        Each time next() is called on it, the generator resumes where it left off
            (it remembers all the data values and which statement was last executed).
        """
        for i in range(len(self.collection) - 1, -1, -1):
            yield self.collection[i]

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
    for v in obj.reverse_generator():
        print(v, end=" ")
    print()

    print(obj)
