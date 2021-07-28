#!/usr/bin/env python
# coding: utf-8

from src.practices.search.algo.linear import linear_search
from src.practices.search.algo.binary import binary_search


def scan_inputs():
    l = int(input())
    arr = []
    if l <= 0:
        l = 20
        arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    else:
        for i in range(l):
            v = int(input())
            arr.append(v)

    search_val = int(input())
    return arr, l, search_val


if __name__ == '__main__':
    array, length, search_val = scan_inputs()

    print(linear_search(array, length, search_val))
    print(binary_search(array, length, search_val))
