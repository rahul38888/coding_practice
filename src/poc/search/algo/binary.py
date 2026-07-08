def part_search(sorted_array,s,e,val):
    if s > e:
        return -1

    mid=int((s+e)/2)
    if sorted_array[mid]==val:
        return mid
    elif sorted_array[mid]>val:
        return part_search(sorted_array,s,mid-1,val)
    else:
        return part_search(sorted_array,mid+1,e,val)


def binary_search(sorted_array, l, val):
    if l == 0:
        return -1
    return part_search(sorted_array, 0, l-1, val)