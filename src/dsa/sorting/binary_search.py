
class BinarySearch:
    def __init__(self, array: list[int], decreasing):
        self.__decreasing = decreasing
        self.__array = self.__merge_sort(array, 0, len(array) - 1)

    def __merge(self, arr1: list[int], arr2: list[int]):
        result = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if self.__decreasing:
                    result.append(arr2[j])
                    j += 1
                else:
                    result.append(arr1[i])
                    i += 1

            else:
                if self.__decreasing:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

    def __merge_sort(self,    array: list[int], s: int, e: int) -> list[int]:
        if s == e:
            return [array[s]]

        m = (s + e )//2
        left = self.__merge_sort(array, s, m)
        right = self.__merge_sort(array, m + 1, e)

        return self.__merge(left, right)

    def contains(self, value: int) -> bool:
        s = 0
        e = len(self.__array) - 1
        while s <= e:
            m = (s + e)//2
            if self.__array[m] == value:
                return True
            elif self.__array[m] < value:
                if self.__decreasing:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if self.__decreasing:
                    s = m + 1
                else:
                    e = m - 1

        return False

    def get_position(self, value: int, most_right: bool = True) -> int:
        s = 0
        e = len(self.__array) - 1

        while s <= e:
            m = (s + e)//2
            if self.__array[m] == value:
                if most_right:
                    s = m + 1
                else:
                    e = m - 1
            elif self.__array[m] < value:
                if self.__decreasing:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if self.__decreasing:
                    s = m + 1
                else:
                    e = m - 1

        return e + 1

    def print(self):
        print("Decreasing: " if self.__decreasing else "Increasing:", self.__array)


if __name__ == '__main__':
    arr = [1, 4, 5, 9, 0, 3, 5, 7, 8]
    inc = BinarySearch(arr, False)
    dec = BinarySearch(arr, True)

    inc.print()
    dec.print()

    print("+++++++++++++++++")
    print("+++++++++++++++++")

    val = 4
    print(f"{val} in inc: {inc.contains(val)}, {val} in dec: {dec.contains(val)}")
    print(f"{val} rightmost loc in inc: {inc.get_position(val)}")
    print(f"{val} leftmost loc in inc: {inc.get_position(val, False)}")

    print(f"{val} rightmost loc in dec: {dec.get_position(val)}")
    print(f"{val} leftmost loc in dec: {dec.get_position(val, False)}")
    print("-----------------")

    val = 5
    print(f"{val} in inc: {inc.contains(val)}, {val} in dec: {dec.contains(val)}")
    print(f"{val} rightmost loc in inc: {inc.get_position(val)}")
    print(f"{val} leftmost loc in inc: {inc.get_position(val, False)}")

    print(f"{val} rightmost loc in dec: {dec.get_position(val)}")
    print(f"{val} leftmost loc in dec: {dec.get_position(val, False)}")
    print("-----------------")

    val = 2
    print(f"{val} in inc: {inc.contains(val)}, {val} in dec: {dec.contains(val)}")
    print(f"{val} rightmost loc in inc: {inc.get_position(val)}")
    print(f"{val} leftmost loc in inc: {inc.get_position(val, False)}")

    print(f"{val} rightmost loc in dec: {dec.get_position(val)}")
    print(f"{val} leftmost loc in dec: {dec.get_position(val, False)}")
    print("-----------------")

    val = -1
    print(f"{val} in inc: {inc.contains(val)}, {val} in dec: {dec.contains(val)}")
    print(f"{val} rightmost loc in inc: {inc.get_position(val)}")
    print(f"{val} leftmost loc in inc: {inc.get_position(val, False)}")

    print(f"{val} rightmost loc in dec: {dec.get_position(val)}")
    print(f"{val} leftmost loc in dec: {dec.get_position(val, False)}")
    print("-----------------")

    val = 100
    print(f"{val} in inc: {inc.contains(val)}, {val} in dec: {dec.contains(val)}")
    print(f"{val} rightmost loc in inc: {inc.get_position(val)}")
    print(f"{val} leftmost loc in inc: {inc.get_position(val, False)}")

    print(f"{val} rightmost loc in dec: {dec.get_position(val)}")
    print(f"{val} leftmost loc in dec: {dec.get_position(val, False)}")
    print("-----------------")


